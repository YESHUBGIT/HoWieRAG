from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from howie_rag.core.schemas import Chunk


@dataclass
class RetrievalMatch:
    chunk: Chunk
    score: float


class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str, chunks: List[Chunk], top_k: int = 3) -> List[RetrievalMatch]:
        raise NotImplementedError
