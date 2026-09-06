
from fastapi import APIRouter
from pydantic import BaseModel
from ai.agents.image_agent import ImageAgent

router = APIRouter()
agent = ImageAgent()

class ImageRequest(BaseModel):
    prompt: str
    style: str = "photorealistic"

@router.post("/image/generate")
async def gen(req: ImageRequest):
    return await agent.generate(req.prompt, req.style)
