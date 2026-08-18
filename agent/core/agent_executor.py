from typing import Any

from .agent_registry import AgentRegistry


class AgentExecutor:
    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def execute(self, agent_name: str, *args: Any, **kwargs: Any) -> Any:
        agent = self.registry.get(agent_name)

        if agent is None:
            raise ValueError(f"Agent not found: {agent_name}")

        if agent.handler is None:
            raise ValueError(f"Agent has no handler: {agent_name}")

        return agent.handler(*args, **kwargs)
