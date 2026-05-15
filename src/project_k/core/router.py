from __future__ import annotations

import re

from project_k.core.models import ExecutionTarget, RouteDecision, TaskCategory
from project_k.core.policy import impact_for


CODE_KEYWORDS = {
    "code",
    "python",
    "bug",
    "test",
    "tests",
    "refactor",
    "implement",
    "repo",
    "module",
    "function",
    "cli",
    "program",
}
RESEARCH_KEYWORDS = {
    "research",
    "investigate",
    "source",
    "sources",
    "citation",
    "citations",
    "current",
    "latest",
    "buscar",
    "investiga",
}
DOCUMENT_KEYWORDS = {
    "document",
    "documents",
    "pdf",
    "docx",
    "pptx",
    "xlsx",
    "summary",
    "summarize",
    "notes",
    "entregable",
}
LOCAL_FILE_KEYWORDS = {
    "folder",
    "file",
    "files",
    "directory",
    "scan",
    "organize",
    "local",
    "carpeta",
    "archivo",
    "archivos",
}
AUTOMATION_KEYWORDS = {
    "automate",
    "automation",
    "schedule",
    "daily",
    "workflow",
    "remind",
    "monitor",
    "watch",
}
CONVERSATION_KEYWORDS = {"hello", "hi", "hola", "thanks", "gracias", "chat"}


def route_task(task: str) -> RouteDecision:
    normalized_task = " ".join(task.split())
    category = classify_task(normalized_task)
    return _decision_for(normalized_task, category)


def classify_task(task: str) -> TaskCategory:
    tokens = set(re.findall(r"[a-z0-9_]+", task.casefold()))

    if tokens & CODE_KEYWORDS:
        return TaskCategory.CODE
    if tokens & RESEARCH_KEYWORDS:
        return TaskCategory.RESEARCH
    if tokens & DOCUMENT_KEYWORDS:
        return TaskCategory.DOCUMENTS
    if tokens & LOCAL_FILE_KEYWORDS:
        return TaskCategory.LOCAL_FILES
    if tokens & AUTOMATION_KEYWORDS:
        return TaskCategory.AUTOMATION
    if tokens and tokens <= CONVERSATION_KEYWORDS:
        return TaskCategory.CONVERSATION
    return TaskCategory.UNKNOWN


def _decision_for(task: str, category: TaskCategory) -> RouteDecision:
    task_text = task or "(empty task)"

    decisions = {
        TaskCategory.CODE: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.86,
            target=ExecutionTarget.SPECIALIST_AGENT,
            impact=impact_for(category),
            reason="Dry-run classification: code work is a future specialist-agent candidate, likely via ACP, before spending cloud tokens.",
            next_step="Ask for the repository scope and produce a concrete implementation plan before invoking any coding agent.",
        ),
        TaskCategory.RESEARCH: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.82,
            target=ExecutionTarget.CLOUD_MODEL,
            impact=impact_for(category),
            reason="Dry-run classification: research often needs current sources and may justify network or cloud escalation.",
            next_step="Confirm whether network access and cloud-backed reasoning are allowed for this task.",
        ),
        TaskCategory.DOCUMENTS: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.80,
            target=ExecutionTarget.LOCAL_MODEL,
            impact=impact_for(category),
            reason="Dry-run classification: document workflows should start locally and only escalate if extraction or reasoning quality is insufficient.",
            next_step="Ask for the document path, output format, and permission before reading or writing files.",
        ),
        TaskCategory.LOCAL_FILES: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.78,
            target=ExecutionTarget.LOCAL_MODEL,
            impact=impact_for(category),
            reason="Dry-run classification: local file work should stay private and bounded to an explicit path scope.",
            next_step="Request the exact directory scope and whether the first pass must be read-only.",
        ),
        TaskCategory.AUTOMATION: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.74,
            target=ExecutionTarget.HUMAN_CLARIFICATION,
            impact=impact_for(category),
            reason="Dry-run classification: automation changes can persist beyond one command and need schedule, scope, and consent.",
            next_step="Ask for trigger, frequency, allowed actions, and stop conditions before creating automation.",
        ),
        TaskCategory.CONVERSATION: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.70,
            target=ExecutionTarget.NO_MODEL_NEEDED,
            impact=impact_for(category),
            reason="Dry-run classification: casual conversation needs no tool, filesystem, network, MCP, ACP, or cloud execution.",
            next_step="Respond locally without invoking tools or providers.",
        ),
        TaskCategory.UNKNOWN: RouteDecision(
            task=task_text,
            category=category,
            confidence=0.20,
            target=ExecutionTarget.HUMAN_CLARIFICATION,
            impact=impact_for(category),
            reason="Dry-run classification: the task is ambiguous and the router should not guess a costly or risky path.",
            next_step="Ask one clarifying question about the desired outcome, data scope, and allowed execution level.",
        ),
    }
    return decisions[category]

