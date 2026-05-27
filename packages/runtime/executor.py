from typing import List
from packages.core.engine import Engine
from packages.core.types import Agent, Task

class Executor:
    def __init__(self, agents: List[Agent]) -> None:
        self.engine = Engine(agents)

    def run(self) -> None:
        self.engine.process_message_queue()

    def add_task(self, task: Task) -> None:
        self.engine.add_task(task)

    def get_tasks(self) -> List[Task]:
        return self.engine.get_tasks()
