from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class LLMProvider:
    name: str
    model: str
    handler: Callable[..., Any] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class LLMRouter:
    def __init__(self):
        self._providers: dict[str, LLMProvider] = {}

    def register(self, provider: LLMProvider) -> None:
        key = provider.name.strip().lower()

        if not key:
            raise ValueError("Provider name cannot be empty.")

        self._providers[key] = provider

    def unregister(self, name: str) -> None:
        self._providers.pop(name.strip().lower(), None)

    def get(self, name: str) -> LLMProvider | None:
        return self._providers.get(name.strip().lower())

    def list_providers(self) -> list[LLMProvider]:
        return list(self._providers.values())

    def route(
        self,
        provider_name: str,
        prompt: str,
        **kwargs: Any,
    ) -> Any:
        provider = self.get(provider_name)

        if provider is None:
            raise ValueError(f"LLM provider not found: {provider_name}")

        if provider.handler is None:
            raise ValueError(f"LLM provider has no handler: {provider_name}")

        return provider.handler(
            prompt=prompt,
            model=provider.model,
            **kwargs,
        )
