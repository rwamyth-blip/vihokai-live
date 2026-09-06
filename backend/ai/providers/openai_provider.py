from .base_provider import BaseProvider
import os
from openai import AsyncOpenAI

class OpenaiProviderProvider(BaseProvider):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY") or "dummy-key-for-dev"
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.is_dev_mode = "dummy" in self.client.api_key

    async def generate(self, prompt: str, system_prompt: str = None, **kwargs):
        # ถ้าเป็นโหมด DEV ให้ตอบ Mock
        if self.is_dev_mode:
            return f"[MOCK {self.__class__.__name__}] คำตอบสำหรับ '{prompt[:80]}...' นี่คือคำตอบจำลอง เมื่อใส่ API KEY จริงจะได้คำตอบจริง"
        
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            completion = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=kwargs.get("temperature", 0.7),
                max_tokens=kwargs.get("max_tokens", 2000)
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI: {str(e)}"