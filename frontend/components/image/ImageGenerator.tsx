
"use client";
import { useState } from "react";
export default function ImageGenerator({ apiUrl }: { apiUrl: string }) {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const handleGen = async () => {
    setLoading(true);
    const res = await fetch(`${apiUrl}/image/generate`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ prompt }) });
    setResult(await res.json()); setLoading(false);
  };
  return (
    <div className="space-y-4">
      <div className="flex gap-2"><input value={prompt} onChange={e=>setPrompt(e.target.value)} placeholder="บ้านโมเดิร์น 2 ชั้น..." className="flex-1 p-3 rounded-xl bg-zinc-900 border border-zinc-800" /><button onClick={handleGen} className="px-6 rounded-xl bg-white text-black font-bold">{loading?"Enhancing...":"Generate"}</button></div>
      {result && (<div className="grid grid-cols-2 gap-4"><div className="p-4 rounded-xl bg-zinc-900 border"><p className="text-xs text-zinc-400">ENHANCED BY {result.enhanced_by}</p><p className="text-sm text-cyan-300 mt-2">{result.enhanced_prompt}</p></div><img src={result.image_url} className="rounded-xl border" /></div>)}
    </div>
  )
}
