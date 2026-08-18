from typing import Any

from .agent_executor import AgentExecutor
from .agent_registry import AgentDefinition, AgentRegistry


class AgentManager:
    def __init__(self, registry: AgentRegistry | None = None):
        self.registry = registry or AgentRegistry()
        self.executor = AgentExecutor(self.registry)

    def register(self, agent: AgentDefinition) -> None:
        self.registry.register(agent)

    def execute(self, agent_name: str, *args: Any, **kwargs: Any) -> Any:
        return self.executor.execute(agent_name, *args, **kwargs)

    def list_agents(self) -> list[AgentDefinition]:
        return self.registry.list_agents()
