from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .memory_storage import MemoryStorage
from .sqlite_memory_storage import SQLiteMemoryStorage


@dataclass
class MemoryEntry:
    content: Any
    memory_type: str = "short_term"
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)


class MemoryManager:
    def __init__(self, storage: MemoryStorage | None = None):
        self.storage = storage or SQLiteMemoryStorage()

    def store(
        self,
        content: Any,
        memory_type: str = "short_term",
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        entry = MemoryEntry(
            content=content,
            memory_type=memory_type,
            metadata=metadata or {},
        )
        self.storage.save(entry)
        return entry

    def get_all(self) -> list[Any]:
        return self.storage.load_all()

    def get_by_type(self, memory_type: str) -> list[Any]:
        memory_type = memory_type.strip().lower()
        return [
            memory
            for memory in self.get_all()
            if memory["memory_type"].lower() == memory_type
        ]

    def clear(self) -> None:
        self.storage.clear()
