import asyncio

class LanguageDetectionAnalyzer:
    name = "LangDetect"
    version = "1.0"
    description = "Detects language (simulated)"
    is_async = True

    def analyze(self, text: str):
        return {"language": "en"}  # fallback

    async def analyze_async(self, text: str):
        await asyncio.sleep(0.1)  # simulate async work
        return {"language": "en"}
