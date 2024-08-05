from __future__ import annotations

import bentoml
from typing import List

@bentoml.service
class Summarization:
    def __init__(self) -> None:
        from transformers import pipeline
        self.pipeline = pipeline('summarization')

    @bentoml.api(batchable=True)
    def summarize(self, texts: List[str]) -> List[str]:
        results = self.pipeline(texts)
        return [item['summary_text'] for item in results]


