# ไฟล์: backend/ai/orchestrator.py

import asyncio
from .router import AIRouter
from .providers import gemini, openai_provider, deepseek, meta_ai, kimi_provider
from .agents.judge_agent import JudgeAgent

class AIOrchestrator:
    def __init__(self):
        self.router = AIRouter()
        self.providers = {
            "gemini": gemini.GeminiProvider(),
            "chatgpt": openai_provider.OpenaiProviderProvider(),  # ✅ ชื่อที่ถูกต้อง
            "deepseek": deepseek.DeepseekProvider(),
            "kimi": kimi_provider.KimiProviderProvider(),  # ✅ น่าจะเป็นแบบนี้ด้วย
            "meta_ai": meta_ai.MetaAIProvider(),
        }
        self.judge = JudgeAgent()

    async def _call(self, name, prompt, **kwargs):
        try:
            p = self.providers[name]
            result = await asyncio.wait_for(p.generate(prompt, **kwargs), timeout=40)
            return name, {"status": "success", "answer": result}
        except Exception as e:
            return name, {"status": "error", "answer": str(e)}

    async def run(self, question: str, mode="single", selected_ai="auto"):
        target_ais = self.router.route(question, user_choice=selected_ai)
        if mode == "single":
            name = target_ais[0]
            _, res = await self._call(name, question)
            return {"mode": "single", "best_ai": name, "answer": res["answer"], "all_answers": {name: res["answer"]}}

        if mode == "synthesize":
            target_ais = ["chatgpt", "gemini", "deepseek", "kimi", "meta_ai"]

        tasks = [self._call(n, question) for n in target_ais]
        results = await asyncio.gather(*tasks)
        all_answers = {name: data["answer"] for name, data in results if data["status"]=="success"}

        if mode == "compare":
            return {"mode": "compare", "all_answers": all_answers, "question": question}

        final = await self.judge.synthesize(question, all_answers)
        return {"mode": "synthesize", "all_answers": all_answers, "final_answer": final, "judge_by": "meta_ai (Llama 3.3 70B)"}