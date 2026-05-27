from packages.core import Engine

class OrchestratorService:
    def __init__(self):
        self.engine = Engine([])

    def register_agent(self, agent):
        self.engine.register_agent(agent)

    def execute_task(self, task):
        self.engine.execute(task)