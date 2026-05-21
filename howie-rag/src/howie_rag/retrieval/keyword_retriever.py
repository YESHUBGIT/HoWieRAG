import re
from dataclasses import dataclass
from typing import List

from howie_rag.core.schemas import Chunk


_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "do",
    "in",
    "is",
    "the",
    "to",
    "we",
    "what",
}


@dataclass
class RetrievalMatch:
    chunk: Chunk
    score: int


def _tokenize(text: str) -> List[str]:
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [token for token in tokens if token not in _STOPWORDS]


def _score_chunk(query: str, chunk: Chunk) -> int:
    query_tokens = set(_tokenize(query))
    chunk_tokens = set(_tokenize(chunk.text))
    return len(query_tokens & chunk_tokens)


def retrieve_chunks(query: str, chunks: List[Chunk], top_k: int = 3) -> List[RetrievalMatch]:
    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    matches: List[RetrievalMatch] = []
    for chunk in chunks:
        score = _score_chunk(query, chunk)
        if score > 0:
            matches.append(RetrievalMatch(chunk=chunk, score=score))

    matches.sort(key=lambda match: match.score, reverse=True)
    return matches[:top_k]
