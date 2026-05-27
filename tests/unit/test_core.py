import unittest
from packages.core import Agent, Task, Engine

class TestCore(unittest.TestCase):
    def test_agent_registration(self):
        engine = Engine([])
        agent = Agent('agent-1', 'Agent 1')
        engine.register_agent(agent)
        self.assertIn(agent, engine.agents)

    def test_task_execution(self):
        engine = Engine([])
        agent = Agent('agent-1', 'Agent 1')
        engine.register_agent(agent)
        task = Task('task-1', 'agent-1', {})
        engine.execute(task)
        self.assertIn(task, engine.tasks)