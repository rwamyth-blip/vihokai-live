
"use client";
import ReactMarkdown from "react-markdown";
export function ResearchReport({ data }: { data: any }) {
  if (!data) return null;
  return (<div className="w-full rounded-[20px] border border-zinc-800 bg-zinc-950 p-8"><div className="text-xs text-cyan-300 mb-4">{data.generated_by}</div><h1 className="text-2xl font-bold mb-6">{data.question}</h1><div className="prose prose-invert max-w-none"><ReactMarkdown>{data.report}</ReactMarkdown></div></div>)
}
