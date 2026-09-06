
import os
from openai import AsyncOpenAI
from..providers.meta_ai import MetaAIProvider

class ImageAgent:
    def __init__(self):
        self.meta = MetaAIProvider()
        self.image_client = None
        try:
            if os.getenv("OPENAI_API_KEY") and "your" not in os.getenv("OPENAI_API_KEY",""):
                self.image_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        except: pass

    async def enhance_prompt(self, user_prompt: str) -> str:
        system = "You are prompt engineer. Enhance user prompt to ultra-detailed professional prompt for Flux/SDXL. Return ONLY enhanced prompt."
        enhanced = await self.meta.generate(prompt=user_prompt, system_prompt=system)
        return enhanced

    async def generate(self, user_prompt: str, style: str = "photorealistic"):
        enhanced = await self.enhance_prompt(f"{user_prompt}, {style}")
        image_url = "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9"
        if self.image_client:
            try:
                img = await self.image_client.images.generate(model="dall-e-3", prompt=enhanced, size="1024x1024")
                image_url = img.data[0].url
            except Exception as e:
                print(e)
        return {"original_prompt": user_prompt, "enhanced_prompt": enhanced, "enhanced_by": "Meta AI Llama 3.3", "image_url": image_url}
