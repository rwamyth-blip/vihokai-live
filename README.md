
# AI SUPER SEARCH PLATFORM - V1.1 with Meta AI Core

Platform ที่รวม Search + Chat + Research + Image ในระบบเดียว
โดยมี **Meta AI (Llama 3.3 70B via Groq)** เป็นแกนหลัก 3 หน้าที่:
1. Chat Provider
2. Prompt Enhancer (Image)
3. Judge & Report Writer

## โครงสร้าง
```
ai_super_platform/
├── backend/ (FastAPI + Orchestrator + 3 Agents)
├── frontend/ (Next.js + CompareGrid + ResearchReport + ImageGenerator)
├── docker-compose.yml
└── .env
```

## วิธีรัน (1 คำสั่ง)
1. แก้ไฟล์ `.env` ใส่ GROQ_API_KEY (สมัครฟรีที่ https://console.groq.com)
2. รัน:
```bash
docker compose up --build
```
3. เปิด:
- Frontend: http://localhost:3000
- Backend Docs: http://localhost:8000/docs

## API สำคัญ
- POST /api/chat -> mode: single | compare | synthesize
- POST /api/image/generate
- POST /api/research

## V1.1 Features
- [x] AI Router (Auto routing)
- [x] Parallel Call 5 AIs
- [x] Meta AI Judge Agent
- [x] Image Enhancer by Llama Vision
- [x] Research Agent 8 บท
