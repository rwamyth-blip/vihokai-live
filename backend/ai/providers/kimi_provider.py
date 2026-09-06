from .base_provider import BaseProvider
import os
from openai import AsyncOpenAI

class KimiProviderProvider(BaseProvider):
    def __init__(self):
        api_key = os.getenv("KIMI_API_KEY") or "dummy-key-for-dev"
        base_url = os.getenv("KIMI_BASE_URL", "https://api.moonshot.ai/v1")
        
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = os.getenv("KIMI_MODEL", "moonshot-v1-8k")
        self.is_dev_mode = "dummy" in self.client.api_key

    async def generate(self, prompt: str, system_prompt: str = None, **kwargs):
        if self.is_dev_mode:
            return f"[MOCK {self.__class__.__name__}] คำตอบสำหรับ '{prompt[:80]}...' นี่คือคำตอบจำลอง เมื่อใส่ API KEY จริงจะได้คำตอบจริง"
        
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            # กำหนด temperature ให้เหมาะสมกับโมเดล
            temperature = kwargs.get("temperature", 0.7)
            # ถ้าเป็น kimi-k3 ต้องใช้ temperature = 1 เท่านั้น
            if self.model == "kimi-k3":
                temperature = 1.0
            
            completion = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=kwargs.get("max_tokens", 2000)
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error calling Kimi: {str(e)}"