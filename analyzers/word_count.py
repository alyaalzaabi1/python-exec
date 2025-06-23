class WordCountAnalyzer:
    name = "WordCount"
    version = "1.0"
    description = "Counts the number of words in the text."
    is_async = False

    def analyze(self, text: str):
        return {"word_count": len(text.split())}

    async def analyze_async(self, text: str):
        return self.analyze(text)  # fallback for async
