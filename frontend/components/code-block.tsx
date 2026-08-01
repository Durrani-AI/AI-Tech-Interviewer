"use client";

import React, { useState } from "react";
import { cn } from "@/lib/utils";

interface CodeBlockProps {
  code: string;
  language?: string;
  maxHeight?: string;
  className?: string;
}

export function CodeBlock({ code, language = "python", maxHeight = "350px", className }: CodeBlockProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className={cn("relative rounded-lg border border-surface-border bg-surface-card overflow-hidden group", className)}>
      <div className="flex items-center justify-between px-3 py-1.5 border-b border-surface-border bg-surface/80 text-xs text-foreground-muted">
        <span className="font-mono text-[11px] uppercase tracking-wider">{language}</span>
        <button
          onClick={handleCopy}
          className="hover:text-foreground transition-colors px-2 py-0.5 rounded bg-surface-border/30 hover:bg-surface-border/60 text-[11px]"
        >
          {copied ? "Copied!" : "Copy"}
        </button>
      </div>
      <div className="overflow-auto p-4 font-mono text-xs leading-relaxed text-foreground" style={{ maxHeight }}>
        <pre className="whitespace-pre-wrap break-words">{code}</pre>
      </div>
    </div>
  );
}

export default CodeBlock;
