from howie_rag.core.schemas import IntentResult
from howie_rag.intent.base import BaseIntentClassifier
from howie_rag.intent.intent_labels import IntentLabel


class RuleBasedIntentClassifier(BaseIntentClassifier):
    _KEYWORDS_BY_INTENT: list[tuple[IntentLabel, tuple[str, ...]]] = [
        (
            IntentLabel.COMPARISON,
            (
                "compare",
                "comparison",
                "difference",
                "differences",
                "similarities",
                "versus",
                "vs",
                "between",
                "differ",
            ),
        ),
        (
            IntentLabel.NAVIGATION,
            (
                "where can i find",
                "source",
                "document",
                "report",
                "page",
                "link",
                "citation",
                "which paper",
                "which study",
            ),
        ),
        (
            IntentLabel.LIMITATION,
            (
                "limitation",
                "limitations",
                "caveat",
                "bias",
                "uncertainty",
                "weakness",
                "cannot conclude",
            ),
        ),
        (
            IntentLabel.METHOD_CONTEXT,
            (
                "method",
                "methodology",
                "sample",
                "survey design",
                "data collection",
                "participants",
                "research design",
                "how was the data collected",
            ),
        ),
        (
            IntentLabel.SUMMARY,
            (
                "summarize",
                "summary",
                "overview",
                "key findings",
                "main findings",
                "main points",
                "what are the findings",
            ),
        ),
        (
            IntentLabel.FACT,
            (
                "what is",
                "what was",
                "when",
                "where",
                "how many",
                "how much",
                "which result",
                "what percentage",
                "sample size",
            ),
        ),
    ]

    def classify(self, question: str) -> IntentResult:
        normalized_question = question.lower()

        for intent, keywords in self._KEYWORDS_BY_INTENT:
            for keyword in keywords:
                if keyword in normalized_question:
                    return IntentResult(
                        intent=intent.value,
                        confidence=0.9,
                        reasoning=f"Matched keyword: '{keyword}'",
                    )

        return IntentResult(
            intent=IntentLabel.UNKNOWN.value,
            confidence=0.2,
            reasoning="No keyword matched.",
        )
