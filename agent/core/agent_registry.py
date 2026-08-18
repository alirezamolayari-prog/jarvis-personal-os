from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AgentDefinition:
    name: str
    description: str
    capabilities: list[str] = field(default_factory=list)
    handler: Callable[..., Any] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class AgentRegistry:
    def __init__(self):
        self._agents: dict[str, AgentDefinition] = {}

    def register(self, agent: AgentDefinition) -> None:
        key = agent.name.strip().lower()
        if not key:
            raise ValueError("Agent name cannot be empty.")
        self._agents[key] = agent

    def unregister(self, name: str) -> None:
        self._agents.pop(name.strip().lower(), None)

    def get(self, name: str) -> AgentDefinition | None:
        return self._agents.get(name.strip().lower())

    def list_agents(self) -> list[AgentDefinition]:
        return list(self._agents.values())

    def find_by_capability(self, capability: str) -> list[AgentDefinition]:
        capability = capability.strip().lower()
        return [
            agent
            for agent in self._agents.values()
            if capability in {item.lower() for item in agent.capabilities}
        ]

    def __contains__(self, name: str) -> bool:
        return name.strip().lower() in self._agents
