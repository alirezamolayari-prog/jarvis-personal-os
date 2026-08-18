from typing import Any

from agent.core.agent_manager import AgentManager
from memory.core.memory_manager import MemoryManager


class JarvisOrchestrator:
    def __init__(
        self,
        agent_manager: AgentManager | None = None,
        memory_manager: MemoryManager | None = None,
    ):
        self.agents = agent_manager or AgentManager()
        self.memory = memory_manager or MemoryManager()

    def remember(
        self,
        content: Any,
        memory_type: str = "short_term",
        metadata: dict[str, Any] | None = None,
    ) -> Any:
        return self.memory.store(content, memory_type, metadata)

    def execute_agent(
        self,
        agent_name: str,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        return self.agents.execute(agent_name, *args, **kwargs)

    def list_agents(self):
        return self.agents.list_agents()

    def get_memories(self):
        return self.memory.get_all()
