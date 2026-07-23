from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Agent:
    id: str
    name: str

    def execute(self, task: 'Task') -> None:
        # This is a placeholder for the actual execution logic
        pass

@dataclass
class Task:
    id: str
    agent_id: str
    state: Dict

@dataclass
class MemoryGraph:
    states: Dict[str, Dict]

# Added init to MemoryGraph to prevent KeyError
@dataclass
class MemoryGraph:
    def __init__(self):
        self.states = {}

    def update(self, task_id: str, state: Dict) -> None:
        self.states[task_id] = state

    def get_state(self, task_id: str) -> Dict:
        return self.states.get(task_id, {})
