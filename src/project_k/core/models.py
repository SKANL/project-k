from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class TaskCategory(StrEnum):
    CODE = "code"
    RESEARCH = "research"
    DOCUMENTS = "documents"
    LOCAL_FILES = "local_files"
    AUTOMATION = "automation"
    CONVERSATION = "conversation"
    UNKNOWN = "unknown"


class ExecutionTarget(StrEnum):
    LOCAL_MODEL = "local_model"
    CLOUD_MODEL = "cloud_model"
    SPECIALIST_AGENT = "specialist_agent"
    HUMAN_CLARIFICATION = "human_clarification"
    NO_MODEL_NEEDED = "no_model_needed"


@dataclass(frozen=True)
class PolicyImpact:
    cost: str
    privacy: str
    requires_network: bool = False
    requires_filesystem: bool = False
    requires_confirmation: bool = False
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class RouteDecision:
    task: str
    category: TaskCategory
    confidence: float
    target: ExecutionTarget
    impact: PolicyImpact
    reason: str
    next_step: str

    @property
    def cost(self) -> str:
        return self.impact.cost

    @property
    def privacy(self) -> str:
        return self.impact.privacy

    @property
    def requires_network(self) -> bool:
        return self.impact.requires_network

    @property
    def requires_filesystem(self) -> bool:
        return self.impact.requires_filesystem

    @property
    def requires_confirmation(self) -> bool:
        return self.impact.requires_confirmation

    @property
    def warnings(self) -> tuple[str, ...]:
        return self.impact.warnings

    def to_dict(self) -> dict[str, Any]:
        return {
            "task": self.task,
            "category": self.category.value,
            "confidence": self.confidence,
            "target": self.target.value,
            "cost": self.cost,
            "privacy": self.privacy,
            "requires_network": self.requires_network,
            "requires_filesystem": self.requires_filesystem,
            "requires_confirmation": self.requires_confirmation,
            "reason": self.reason,
            "warnings": list(self.warnings),
            "next_step": self.next_step,
        }

