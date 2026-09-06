
class BaseProvider:
    async def generate(self, prompt: str, system_prompt: str = None, **kwargs):
        raise NotImplementedError
