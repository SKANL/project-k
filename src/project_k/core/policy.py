from __future__ import annotations

from project_k.core.models import PolicyImpact, TaskCategory


def impact_for(category: TaskCategory) -> PolicyImpact:
    impacts = {
        TaskCategory.CODE: PolicyImpact(
            cost="optional_paid",
            privacy="local",
            requires_confirmation=True,
            warnings=(
                "Dry-run only: future ACP delegation may invoke a coding agent, but no agent was executed.",
                "Future workspace access requires explicit scope and confirmation.",
            ),
        ),
        TaskCategory.RESEARCH: PolicyImpact(
            cost="optional_paid",
            privacy="cloud",
            requires_network=True,
            requires_confirmation=True,
            warnings=(
                "Research may require network access and cloud model escalation.",
                "Dry-run only: no browser, MCP server, API, or cloud provider was contacted.",
            ),
        ),
        TaskCategory.DOCUMENTS: PolicyImpact(
            cost="free",
            privacy="local",
            requires_filesystem=True,
            requires_confirmation=True,
            warnings=(
                "Document processing may read or write local files in future versions.",
                "Dry-run only: no document or filesystem tool was executed.",
            ),
        ),
        TaskCategory.LOCAL_FILES: PolicyImpact(
            cost="free",
            privacy="local",
            requires_filesystem=True,
            requires_confirmation=True,
            warnings=(
                "Local file workflows require a bounded path scope before execution.",
                "Dry-run only: no local files were read, listed, moved, or modified.",
            ),
        ),
        TaskCategory.AUTOMATION: PolicyImpact(
            cost="free",
            privacy="local",
            requires_confirmation=True,
            warnings=(
                "Automation can become persistent or recurring and needs explicit user confirmation.",
                "Dry-run only: no automation was created, scheduled, or executed.",
            ),
        ),
        TaskCategory.CONVERSATION: PolicyImpact(cost="free", privacy="local"),
        TaskCategory.UNKNOWN: PolicyImpact(
            cost="free",
            privacy="local",
            requires_confirmation=True,
            warnings=("Ambiguous routing could choose the wrong tool, privacy level, or cost path.",),
        ),
    }
    return impacts[category]

