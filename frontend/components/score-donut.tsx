"use client";

import React from "react";
import { cn } from "@/lib/utils";

interface ScoreDonutProps {
  score: number; // 0 to 10
  size?: number; // width & height in px
  strokeWidth?: number;
  showLabel?: boolean;
  className?: string;
}

export function ScoreDonut({
  score,
  size = 80,
  strokeWidth = 7,
  showLabel = true,
  className,
}: ScoreDonutProps) {
  const safeScore = Math.max(0, Math.min(10, score));
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (safeScore / 10) * circumference;

  let colorClass = "text-danger";
  let strokeColor = "#ef4444"; // danger
  if (safeScore >= 7) {
    colorClass = "text-success";
    strokeColor = "#22c55e"; // success
  } else if (safeScore >= 4) {
    colorClass = "text-warning";
    strokeColor = "#eab308"; // warning
  }

  return (
    <div className={cn("relative inline-flex items-center justify-center select-none", className)}>
      <svg width={size} height={size} className="-rotate-90 transform">
        {/* Background Track */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="currentColor"
          strokeWidth={strokeWidth}
          className="text-surface-border opacity-40 fill-none"
        />
        {/* Filled Progress Arc */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={strokeColor}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
          className="fill-none transition-all duration-700 ease-out"
        />
      </svg>
      {showLabel && (
        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
          <span className={cn("font-bold font-mono tracking-tight", size > 100 ? "text-2xl" : size > 60 ? "text-lg" : "text-sm", colorClass)}>
            {safeScore.toFixed(1)}
          </span>
          <span className="text-[10px] text-foreground-muted uppercase font-medium -mt-1">/ 10</span>
        </div>
      )}
    </div>
  );
}

export default ScoreDonut;
