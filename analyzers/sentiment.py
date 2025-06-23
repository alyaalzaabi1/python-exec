class SentimentAnalyzer:
    name = "Sentiment"
    version = "1.0"
    description = "Dummy sentiment analyzer"
    is_async = False

    def analyze(self, text: str):
        sentiment = "positive" if "good" in text else "neutral"
        return {"sentiment": sentiment}

    async def analyze_async(self, text: str):
        return self.analyze(text)
