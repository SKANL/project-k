import contextlib
import io
import json
import pathlib
import tomllib
import unittest

from project_k.interfaces.cli import main


ROOT = pathlib.Path(__file__).resolve().parents[2]


class CliTests(unittest.TestCase):
    def test_json_output_is_valid_and_stable(self):
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            exit_code = main(["--json", "research", "MCP", "servers"])

        self.assertEqual(0, exit_code)
        payload = json.loads(stdout.getvalue())
        self.assertEqual("research MCP servers", payload["task"])
        self.assertEqual("research", payload["category"])
        self.assertIn("requires_network", payload)
        self.assertIn("warnings", payload)

    def test_default_output_is_human_readable_dry_run(self):
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            exit_code = main(["implement", "a", "router"])

        output = stdout.getvalue()
        self.assertEqual(0, exit_code)
        self.assertIn("Project-K Core v0 dry-run", output)
        self.assertIn("Task type:", output)
        self.assertIn("Recommended route:", output)
        self.assertIn("No model, tool, shell, filesystem, MCP, ACP, or cloud action was executed.", output)

    def test_pyproject_script_points_to_interface_cli(self):
        pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

        self.assertEqual("project_k.interfaces.cli:main", pyproject["project"]["scripts"]["project-k"])


if __name__ == "__main__":
    unittest.main()
