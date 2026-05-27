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
