from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from project_k.core.models import RouteDecision
from project_k.core.router import route_task


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="project-k",
        description="Project-K Core v0 dry-run router.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the stable machine-readable route decision contract.",
    )
    parser.add_argument("task", nargs="+", help="Task text to classify.")

    args = parser.parse_args(argv)
    decision = route_task(" ".join(args.task))

    if args.json:
        print(json.dumps(decision.to_dict(), ensure_ascii=False))
    else:
        print(format_human(decision))

    return 0


def format_human(decision: RouteDecision) -> str:
    warnings = "\n".join(f"- {warning}" for warning in decision.warnings) or "- None"
    confirmation = "yes" if decision.requires_confirmation else "no"
    network = "yes" if decision.requires_network else "no"
    filesystem = "yes" if decision.requires_filesystem else "no"

    return "\n".join(
        [
            "Project-K Core v0 dry-run",
            f"Task: {decision.task}",
            f"Task type: {decision.category.value} ({decision.confidence:.2f})",
            f"Recommended route: {decision.target.value}",
            f"Cost: {decision.cost}",
            f"Privacy: {decision.privacy}",
            f"Requires network: {network}",
            f"Requires filesystem: {filesystem}",
            f"Requires confirmation: {confirmation}",
            f"Reason: {decision.reason}",
            "Permission notes:",
            warnings,
            f"Next safe step: {decision.next_step}",
            "No model, tool, shell, filesystem, MCP, ACP, or cloud action was executed.",
        ]
    )


if __name__ == "__main__":
    raise SystemExit(main())
