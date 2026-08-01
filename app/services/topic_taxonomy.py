"""Structured topic taxonomy for coding problem matching.

Maps fuzzy user input to canonical topic categories and provides
related-topic expansion for broader problem matching.
"""

from __future__ import annotations

import re
from typing import Any


# Canonical topic tree: category -> list of subtopics / aliases
TOPIC_TREE: dict[str, list[str]] = {
    "arrays": [
        "array", "two-pointer", "two pointer", "prefix-sum", "prefix sum",
        "kadane", "subarray", "matrix", "2d array", "sorting",
    ],
    "hashing": [
        "hash", "hashmap", "hash map", "hash table", "hashtable",
        "dictionary", "set", "counting",
    ],
    "sliding-window": [
        "sliding window", "window", "substring",
    ],
    "stack": [
        "stack", "monotonic stack", "parentheses", "brackets",
    ],
    "queue": [
        "queue", "deque", "bfs", "breadth-first",
    ],
    "linked-list": [
        "linked list", "linkedlist", "singly linked", "doubly linked",
        "fast slow pointer", "cycle detection",
    ],
    "binary-search": [
        "binary search", "bisect", "search", "sorted array",
    ],
    "trees": [
        "tree", "binary tree", "bst", "binary search tree",
        "dfs", "depth-first", "inorder", "preorder", "postorder",
        "trie", "segment tree", "heap", "priority queue",
    ],
    "graphs": [
        "graph", "shortest path", "dijkstra", "bellman-ford",
        "topological sort", "topological", "union-find", "union find",
        "disjoint set", "connected component", "adjacency",
    ],
    "dynamic-programming": [
        "dynamic programming", "dp", "memoization", "tabulation",
        "knapsack", "lis", "longest increasing", "fibonacci",
        "coin change", "edit distance",
    ],
    "strings": [
        "string", "pattern matching", "anagram", "palindrome",
        "regex", "kmp", "rabin-karp",
    ],
    "greedy": [
        "greedy", "interval", "scheduling", "activity selection",
    ],
    "backtracking": [
        "backtracking", "recursion", "permutation", "combination",
        "subset", "n-queens",
    ],
    "bit-manipulation": [
        "bit", "bitwise", "xor", "bit manipulation",
    ],
    "design": [
        "design", "oop", "object-oriented", "class design",
        "lru", "lfu", "cache", "system",
    ],
    "math": [
        "math", "number theory", "prime", "gcd", "modular",
    ],
}

# Reverse lookup: alias -> canonical category
_ALIAS_TO_CATEGORY: dict[str, str] = {}
for _cat, _aliases in TOPIC_TREE.items():
    _ALIAS_TO_CATEGORY[_cat] = _cat
    for _alias in _aliases:
        _ALIAS_TO_CATEGORY[_alias.lower()] = _cat


def resolve_topic(user_input: str) -> str | None:
    """Map fuzzy user input to a canonical topic category.

    Returns the canonical category name, or None if no match.
    """
    normalized = user_input.strip().lower()
    if not normalized:
        return None

    # Direct match
    if normalized in _ALIAS_TO_CATEGORY:
        return _ALIAS_TO_CATEGORY[normalized]

    # Substring match: check if any alias appears in the user input
    for alias, category in sorted(
        _ALIAS_TO_CATEGORY.items(), key=lambda x: -len(x[0])
    ):
        if alias in normalized:
            return category

    return None


def get_related_topics(topic: str) -> list[str]:
    """Return subtopics/aliases for a canonical category.

    Useful for broadening the search when exact topic match yields no problems.
    """
    category = resolve_topic(topic)
    if category and category in TOPIC_TREE:
        return list(TOPIC_TREE[category])
    return []


def topic_matches_problem(problem: dict[str, Any], user_topic: str) -> bool:
    """Check if a problem matches a user-provided topic.

    Uses the taxonomy for intelligent matching instead of raw string search.
    """
    if not user_topic or not user_topic.strip():
        return True

    category = resolve_topic(user_topic)
    related = get_related_topics(user_topic) if category else []

    # Build searchable text from the problem
    haystack = " ".join([
        str(problem.get("title", "")),
        str(problem.get("statement", "")),
        " ".join(problem.get("topics", []) or []),
        " ".join(problem.get("tags", []) or []),
    ]).lower()

    # Match against canonical category
    if category and category in haystack:
        return True

    # Match against related subtopics
    for alias in related:
        if alias.lower() in haystack:
            return True

    # Fallback: raw substring match (preserves existing behavior)
    return user_topic.strip().lower() in haystack
