"use client"
import { useState, useMemo } from "react"

type Chat = { id: string, title: string, date: string, updatedAt: Date }

const mockChats: Chat[] = [
  { id: "1", title: "แก้ปัญหาแคปหน้าจอ", date: "วันนี้", updatedAt: new Date() },
  { id: "2", title: "Debug meta_ai.py syntax error", date: "วันนี้", updatedAt: new Date() },
  { id: "3", title: "วิเคราะห์ฟังก์ชัน Python", date: "เมื่อวาน", updatedAt: new Date(Date.now() - 86400000) },
  { id: "4", title: "Ads Platform Import Error Fix", date: "เมื่อวาน", updatedAt: new Date(Date.now() - 86400000) },
  { id: "5", title: "เปิดไฟล์ FastAPI", date: "7 วัน", updatedAt: new Date(Date.now() - 3*86400000) },
  { id: "6", title: "สเปกเครื่องคอม AI", date: "7 วัน", updatedAt: new Date(Date.now() - 3*86400000) },
  { id: "7", title: "AI Coding Agent V1", date: "7 วัน", updatedAt: new Date(Date.now() - 5*86400000) },
  { id: "8", title: "BuildCraft Home Platform", date: "7 วัน", updatedAt: new Date(Date.now() - 5*86400000) },
  { id: "9", title: "Ads Platform Code Template", date: "7 วัน", updatedAt: new Date(Date.now() - 6*86400000) },
  { id: "10", title: "Global House Plan Marketplace", date: "30 วัน", updatedAt: new Date(Date.now() - 10*86400000) },
]

export function ChatHistory({ onSelect }: { onSelect?: (id: string)=>void }) {
  const [q, setQ] = useState("")
  
  const filtered = useMemo(()=>{
    if(!q) return mockChats
    return mockChats.filter(c=>c.title.toLowerCase().includes(q.toLowerCase()))
  },[q])

  const groups = {
    "วันนี้": filtered.filter(c=>c.date==="วันนี้"),
    "เมื่อวาน": filtered.filter(c=>c.date==="เมื่อวาน"),
    "7 วัน": filtered.filter(c=>c.date==="7 วัน"),
    "30 วัน": filtered.filter(c=>c.date==="30 วัน"),
  }

  return (
    <div className="w-[280px] md:w-[300px] bg-[#0f0f0f] md:bg-[#171717] text-white h-screen flex flex-col">
      {/* Search - เหมือนรูป */}
      <div className="p-3">
        <div className="relative">
          <span className="absolute left-3.5 top-[11px] text-white/40 text-[14px]">⌕</span>
          <input
            value={q}
            onChange={e=>setQ(e.target.value)}
            placeholder="ค้นหาเนื้อหาแชท..."
            className="w-full bg-[#2a2a2a] rounded-full pl-9 pr-4 py-2.5 text-[13px] placeholder:text-white/40 focus:outline-none focus:bg-[#333]"
          />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto px-2 pb-20">
        {Object.entries(groups).map(([label, items])=>(
          items.length>0 && (
            <div key={label} className="mb-5">
              <div className="flex items-center justify-between px-2 py-1">
                <span className="text-[12px] text-white/40">{label}</span>
                {label==="วันนี้" && <span className="text-white/20 text-[12px]">⫶</span>}
              </div>
              <div className="space-y-0.5">
                {items.map(c=>(
                  <button
                    key={c.id}
                    onClick={()=>onSelect?.(c.id)}
                    className="w-full text-left px-2.5 py-2 rounded-lg hover:bg-white/10 text-[13px] truncate text-white/90 hover:text-white transition"
                  >
                    {c.title}
                  </button>
                ))}
              </div>
            </div>
          )
        ))}
      </div>

      {/* User bottom - เหมือนรูป */}
      <div className="p-3 border-t border-white/10 flex items-center gap-2">
        <div className="w-8 h-8 rounded-full bg-[#8b5cf6] flex items-center justify-center text-[13px] font-bold">M</div>
        <span className="text-[13px]">Modern A</span>
        <span className="ml-auto text-white/30">•••</span>
      </div>
    </div>
  )
}
