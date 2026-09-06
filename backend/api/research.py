
from fastapi import APIRouter
from pydantic import BaseModel
from ai.agents.research_agent import ResearchAgent

router = APIRouter()
agent = ResearchAgent()

class ResearchRequest(BaseModel):
    question: str

@router.post("/research")
async def research(req: ResearchRequest):
    return await agent.research(req.question)
