import unittest
from packages.core import Engine, Agent, Task
from services.orchestrator import OrchestratorService

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        orchestrator = OrchestratorService()
        agent = Agent('agent-1', 'Agent 1')
        orchestrator.register_agent(agent)
        task = Task('task-1', 'agent-1', {})
        orchestrator.execute_task(task)
        self.assertIn(task, orchestrator.engine.tasks)