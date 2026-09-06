
from fastapi import APIRouter
from pydantic import BaseModel
from ai.orchestrator import AIOrchestrator

router = APIRouter()
orchestrator = AIOrchestrator()

class ChatRequest(BaseModel):
    question: str
    mode: str = "synthesize"
    selected_ai: str = "auto"

@router.post("/chat")
async def chat_endpoint(req: ChatRequest):
    result = await orchestrator.run(req.question, mode=req.mode, selected_ai=req.selected_ai)
    return result
