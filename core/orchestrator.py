from typing import Any

from agent.core.agent_manager import AgentManager
from agent.core.llm_router import LLMRouter
from memory.core.memory_manager import MemoryManager


class JarvisOrchestrator:
    def __init__(
        self,
        agent_manager: AgentManager | None = None,
        memory_manager: MemoryManager | None = None,
        llm_router: LLMRouter | None = None,
    ):
        self.agents = agent_manager or AgentManager()
        self.memory = memory_manager or MemoryManager()
        self.llm = llm_router or LLMRouter()

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

    def ask_llm(
        self,
        provider_name: str,
        prompt: str,
        **kwargs: Any,
    ) -> Any:
        return self.llm.route(provider_name, prompt, **kwargs)

    def list_agents(self):
        return self.agents.list_agents()

    def list_llm_providers(self):
        return self.llm.list_providers()

    def get_memories(self):
        return self.memory.get_all()
