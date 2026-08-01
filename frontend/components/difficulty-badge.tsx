"use client";

import React from "react";
import { cn } from "@/lib/utils";
import type { DifficultyLevel } from "@/types";

interface DifficultyBadgeProps {
  level: DifficultyLevel | string;
  className?: string;
  showDot?: boolean;
}

export function DifficultyBadge({ level, className, showDot = true }: DifficultyBadgeProps) {
  const norm = (level || "medium").toLowerCase();

  let styles = "bg-warning/10 text-warning border-warning/20";
  let dotColor = "bg-warning";

  if (norm === "easy") {
    styles = "bg-success/10 text-success border-success/20";
    dotColor = "bg-success";
  } else if (norm === "hard") {
    styles = "bg-danger/10 text-danger border-danger/20";
    dotColor = "bg-danger";
  }

  const label = norm.charAt(0).toUpperCase() + norm.slice(1);

  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold border tracking-wide select-none",
        styles,
        className
      )}
    >
      {showDot && <span className={cn("h-1.5 w-1.5 rounded-full animate-pulse", dotColor)} />}
      {label}
    </span>
  );
}

export default DifficultyBadge;
