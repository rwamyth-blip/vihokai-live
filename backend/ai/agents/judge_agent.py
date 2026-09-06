
from..providers.meta_ai import MetaAIProvider
JUDGE_SYSTEM = "You are META AI JUDGE. Synthesize best answer in Thai from multiple AIs."
class JudgeAgent:
    def __init__(self):
        self.meta = MetaAIProvider()
    async def synthesize(self, question, all_answers: dict):
        formatted = "\n\n".join([f"### {k.upper()}:\n{v}" for k,v in all_answers.items()])
        prompt = f"คำถาม: {question}\n\nคำตอบจาก AI ต่างๆ:\n{formatted}\n\nสรุปเป็น Best Answer ภาษาไทย แบ่งเป็น สรุป, วิเคราะห์, ข้อสรุป"
        return await self.meta.generate(prompt, system_prompt=JUDGE_SYSTEM, model_type="reasoning", temperature=0.3)
