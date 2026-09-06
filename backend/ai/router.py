
class AIRouter:
    def route(self, query, intent="auto", user_choice="auto"):
        if user_choice != "auto":
            return [user_choice]
        return ["chatgpt", "gemini", "deepseek", "kimi", "meta_ai"]
