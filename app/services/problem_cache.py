"""Problem cache service — DB layer for the hybrid problem bank.

Queries the ``cached_problems`` table for previously validated problems
and stores new AI-generated problems after they pass quality checks.
"""

from __future__ import annotations

import logging
import re
from typing import Any

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CachedProblem

logger = logging.getLogger(__name__)


def _problem_id_from_title(title: str) -> str:
    """Generate a URL-friendly slug from a problem title."""
    slug = re.sub(r"[^a-z0-9]+", "-", title.strip().lower()).strip("-")
    return slug or "coding-problem"


def _normalize_language(language: str | None) -> str:
    value = (language or "python").strip().lower()
    _MAP = {"py": "python", "js": "javascript", "ts": "typescript", "golang": "go", "c#": "csharp", "c++": "cpp"}
    return _MAP.get(value, value)


def _language_starter_code(function_name: str, params: list[str], language: str) -> tuple[str, str]:
    """Generate function signature and starter code for a given language."""
    joined = ", ".join(params)

    if language in {"python", "py"}:
        signature = f"def {function_name}({joined}):"
        starter = f"{signature}\n    # Write your solution\n    pass\n"
        return signature, starter

    if language in {"javascript", "js"}:
        signature = f"function {function_name}({joined}) {{"
        starter = f"{signature}\n  // Write your solution\n}}\n"
        return signature, starter

    if language in {"typescript", "ts"}:
        signature = f"function {function_name}({joined}: any): any {{"
        starter = f"{signature}\n  // Write your solution\n}}\n"
        return signature, starter

    if language == "java":
        signature = f"public static Object {function_name}({', '.join('Object ' + p for p in params)})"
        starter = (
            "class Solution {\n"
            f"    {signature} {{\n"
            "        // Write your solution\n"
            "        return null;\n"
            "    }\n"
            "}\n"
        )
        return signature, starter

    signature = f"{function_name}({joined})"
    starter = f"// Implement {signature}\n"
    return signature, starter


async def get_cached_problem(
    *,
    difficulty: str,
    topic: str,
    programming_language: str | None,
    previous_problem_ids: list[str] | None = None,
    db: AsyncSession,
) -> dict[str, Any] | None:
    """Find an unseen cached problem matching difficulty and topic.

    Returns a formatted problem dict ready for the interview flow,
    or None if no matching cached problem is available.
    """
    from app.services.topic_taxonomy import topic_matches_problem

    difficulty_l = difficulty.strip().lower()
    language = _normalize_language(programming_language)
    excluded = set(previous_problem_ids or [])

    # Query all cached problems at this difficulty
    stmt = (
        select(CachedProblem)
        .where(CachedProblem.difficulty == difficulty_l)
        .order_by(CachedProblem.times_served.asc(), CachedProblem.created_at.desc())
    )
    result = await db.execute(stmt)
    candidates = result.scalars().all()

    for row in candidates:
        if row.problem_id in excluded:
            continue

        # Check topic match using the taxonomy
        problem_dict = {
            "title": row.title,
            "statement": row.statement,
            "topics": row.topics or [],
            "tags": row.tags or [],
        }
        if not topic_matches_problem(problem_dict, topic):
            continue

        # Build the response
        fn_name = row.function_name or ""
        params = row.params or []
        signature, starter = ("", "")
        if fn_name and params:
            signature, starter = _language_starter_code(fn_name, params, language)

        # Increment serve count
        await db.execute(
            update(CachedProblem)
            .where(CachedProblem.id == row.id)
            .values(times_served=CachedProblem.times_served + 1)
        )

        logger.info("Serving cached problem: %s (served %d times)", row.problem_id, row.times_served + 1)

        return {
            "title": row.title,
            "problem_id": row.problem_id,
            "statement": row.statement,
            "difficulty": row.difficulty,
            "constraints": list(row.constraints or []),
            "examples": list(row.examples or []),
            "function_name": fn_name,
            "params": list(params),
            "function_signature": row.function_signature or signature,
            "starter_code": row.starter_code or starter,
            "public_test_cases": list(row.public_test_cases or []),
            "tags": list(row.tags or []),
            "expected_time_complexity": row.expected_time_complexity,
            "expected_space_complexity": row.expected_space_complexity,
            "programming_language": language,
            "source": row.source or "cached",
        }

    return None


async def cache_validated_problem(
    problem_data: dict[str, Any],
    *,
    quality_score: float = 0.7,
    db: AsyncSession,
) -> bool:
    """Store a validated AI-generated problem in the cache.

    Returns True if cached successfully, False if duplicate or error.
    """
    problem_id = str(problem_data.get("problem_id") or "").strip()
    if not problem_id:
        problem_id = _problem_id_from_title(str(problem_data.get("title", "untitled")))

    # Check for duplicate
    result = await db.execute(
        select(CachedProblem.id).where(CachedProblem.problem_id == problem_id)
    )
    if result.scalar_one_or_none() is not None:
        logger.debug("Problem %s already cached, skipping", problem_id)
        return False

    try:
        cached = CachedProblem(
            problem_id=problem_id,
            title=str(problem_data.get("title", "Untitled")),
            difficulty=str(problem_data.get("difficulty", "medium")),
            topics=problem_data.get("tags") or [],
            statement=str(problem_data.get("statement", "")),
            constraints=problem_data.get("constraints") or [],
            examples=problem_data.get("examples") or [],
            function_name=problem_data.get("function_name"),
            params=problem_data.get("params") or [],
            function_signature=problem_data.get("function_signature"),
            starter_code=problem_data.get("starter_code"),
            public_test_cases=problem_data.get("public_test_cases") or [],
            hidden_test_cases=problem_data.get("hidden_test_cases") or [],
            tags=problem_data.get("tags") or [],
            expected_time_complexity=problem_data.get("expected_time_complexity"),
            expected_space_complexity=problem_data.get("expected_space_complexity"),
            source="ai_validated",
            quality_score=quality_score,
        )
        db.add(cached)
        await db.flush()
        logger.info("Cached new problem: %s (quality=%.2f)", problem_id, quality_score)
        return True
    except Exception as exc:
        logger.warning("Failed to cache problem %s: %s", problem_id, exc)
        return False


async def increment_served_count(problem_id: str, db: AsyncSession) -> None:
    """Increment the times_served counter for a problem."""
    await db.execute(
        update(CachedProblem)
        .where(CachedProblem.problem_id == problem_id)
        .values(times_served=CachedProblem.times_served + 1)
    )
