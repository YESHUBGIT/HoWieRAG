from pathlib import Path
from typing import List

from howie_rag.core.schemas import Document
from howie_rag.core.utils import stable_id


def load_text_documents(directory_path: str) -> List[Document]:
    directory = Path(directory_path)
    documents: List[Document] = []

    for file_path in sorted(directory.iterdir()):
        if not file_path.is_file() or file_path.suffix.lower() not in {".txt", ".md"}:
            continue

        text = file_path.read_text(encoding="utf-8")
        documents.append(
            Document(
                doc_id=stable_id(f"{file_path.name}:{text}"),
                title=file_path.stem,
                text=text,
                metadata={
                    "source_path": str(file_path),
                    "file_type": file_path.suffix.lower().lstrip("."),
                },
            )
        )

    return documents
