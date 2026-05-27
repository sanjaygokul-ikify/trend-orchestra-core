import logging
from typing import List, Dict
from .types import Agent, Task, MemoryGraph
from .exceptions import AgentError, TaskError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, agents: List[Agent]) -> None:
        self.agents = agents
        self.memory_graph = MemoryGraph()
        self.tasks = []
        self.message_queue = []

    def execute(self, task: Task) -> None:
        try:
            task_id = task.id
            agent = next((a for a in self.agents if a.id == task.agent_id), None)
            if agent is None:
                logger.error(f"Agent not found for task {task_id}")
                raise AgentError(f"Agent not found for task {task_id}")
            agent.execute(task)
            self.memory_graph.update(task_id, task.state)
            self.tasks.append(task)
        except Exception as e:
            logger.error(f"Error executing task {task_id}: {e}")
            raise TaskError(f"Error executing task {task_id}: {e}")

    def register_agent(self, agent: Agent) -> None:
        self.agents.append(agent)
        logger.info(f"Agent {agent.id} registered")

    def get_memory_graph(self) -> MemoryGraph:
        return self.memory_graph

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        logger.info(f"Task {task.id} added")

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def process_message_queue(self) -> None:
        while self.message_queue:
            message = self.message_queue.pop(0)
            try:
                self.handle_message(message)
            except Exception as e:
                logger.error(f"Error handling message: {e}")

    def handle_message(self, message: Dict) -> None:
        task_id = message.get("task_id")
        if task_id:
            task = next((t for t in self.tasks if t.id == task_id), None)
            if task:
                task.state = message.get("state")
                self.memory_graph.update(task_id, task.state)
                logger.info(f"Task {task_id} updated")
        else:
            logger.error(f"Invalid message: {message}")

class MemoryGraph:
    def __init__(self) -> None:
        self.states = {}

    def update(self, task_id: str, state: Dict) -> None:
        self.states[task_id] = state

    def get_state(self, task_id: str) -> Dict:
        return self.states.get(task_id)
