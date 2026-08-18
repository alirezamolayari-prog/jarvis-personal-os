import json
import sqlite3
from dataclasses import asdict
from typing import Any

from .memory_storage import MemoryStorage


class SQLiteMemoryStorage(MemoryStorage):
    def __init__(self, db_path: str = "memory/data/jarvis_memory.db"):
        self.db_path = db_path
        self._initialize()

    def _initialize(self) -> None:
        import os

        directory = os.path.dirname(self.db_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    metadata TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.commit()

    def save(self, memory: Any) -> None:
        data = asdict(memory)

        with sqlite3.connect(self.db_path) as connection:
            connection.execute(
                """
                INSERT INTO memories
                (content, memory_type, metadata, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    str(data["content"]),
                    data["memory_type"],
                    json.dumps(data["metadata"], ensure_ascii=False),
                    data["created_at"].isoformat(),
                ),
            )
            connection.commit()

    def load_all(self) -> list[dict[str, Any]]:
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(
                """
                SELECT id, content, memory_type, metadata, created_at
                FROM memories
                ORDER BY id ASC
                """
            ).fetchall()

        return [
            {
                "id": row[0],
                "content": row[1],
                "memory_type": row[2],
                "metadata": json.loads(row[3]),
                "created_at": row[4],
            }
            for row in rows
        ]

    def clear(self) -> None:
        with sqlite3.connect(self.db_path) as connection:
            connection.execute("DELETE FROM memories")
            connection.commit()
