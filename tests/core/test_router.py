import unittest

from project_k.core.models import ExecutionTarget, TaskCategory
from project_k.core.router import route_task


class RouteTaskTests(unittest.TestCase):
    def test_code_task_routes_to_specialist_agent_dry_run(self):
        decision = route_task("implement a Python CLI and tests")

        self.assertEqual(TaskCategory.CODE, decision.category)
        self.assertIn(decision.target, {ExecutionTarget.SPECIALIST_AGENT, ExecutionTarget.LOCAL_MODEL})
        self.assertFalse(decision.requires_network)
        self.assertTrue(decision.requires_confirmation)
        self.assertIn("ACP", " ".join(decision.warnings))
        self.assertIn("Dry-run", decision.reason)

    def test_research_task_marks_network_and_cloud_risk(self):
        decision = route_task("research current MCP and ACP implementations")

        self.assertEqual(TaskCategory.RESEARCH, decision.category)
        self.assertEqual(ExecutionTarget.CLOUD_MODEL, decision.target)
        self.assertTrue(decision.requires_network)
        self.assertTrue(decision.requires_confirmation)
        self.assertEqual("cloud", decision.privacy)

    def test_document_task_marks_filesystem_confirmation(self):
        decision = route_task("summarize this PDF document")

        self.assertEqual(TaskCategory.DOCUMENTS, decision.category)
        self.assertTrue(decision.requires_filesystem)
        self.assertTrue(decision.requires_confirmation)

    def test_local_file_task_marks_filesystem_confirmation(self):
        decision = route_task("organize files in this local folder")

        self.assertEqual(TaskCategory.LOCAL_FILES, decision.category)
        self.assertTrue(decision.requires_filesystem)
        self.assertTrue(decision.requires_confirmation)

    def test_casual_conversation_routes_without_cloud_or_tools(self):
        decision = route_task("hola gracias")

        self.assertEqual(TaskCategory.CONVERSATION, decision.category)
        self.assertEqual(ExecutionTarget.NO_MODEL_NEEDED, decision.target)
        self.assertFalse(decision.requires_network)
        self.assertFalse(decision.requires_filesystem)
        self.assertFalse(decision.requires_confirmation)

    def test_unknown_ambiguous_task_asks_for_clarification(self):
        decision = route_task("make it better")

        self.assertEqual(TaskCategory.UNKNOWN, decision.category)
        self.assertEqual(ExecutionTarget.HUMAN_CLARIFICATION, decision.target)
        self.assertTrue(decision.requires_confirmation)

    def test_json_contract_has_stable_keys(self):
        decision = route_task("research current MCP implementations")

        self.assertEqual(
            [
                "task",
                "category",
                "confidence",
                "target",
                "cost",
                "privacy",
                "requires_network",
                "requires_filesystem",
                "requires_confirmation",
                "reason",
                "warnings",
                "next_step",
            ],
            list(decision.to_dict().keys()),
        )


if __name__ == "__main__":
    unittest.main()
