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

    def remove_task(self, task_id: str) -> None:
        self.tasks = [task for task in self.tasks if task.id != task_id]
        logger.info(f"Task {task_id} removed")

    def __contains__(self, task_id: str) -> bool:
        return any(task.id == task_id for task in self.tasks)

    def __len__(self) -> int:
        return len(self.tasks)

    def __getitem__(self, task_id: str) -> Task:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task is None:
            raise TaskError(f"Task {task_id} not found")
        return task

    def shutdown(self) -> None:
        logger.info("Shutting down engine")
        self.tasks = []
        self.message_queue = []

    def start(self) -> None:
        logger.info("Starting engine")

    def restart(self) -> None:
        logger.info("Restarting engine")
        self.shutdown()
        self.start()

    def execute_with_error_handling(self, task: Task) -> None:
        try:
            self.execute(task)
        except TaskError as e:
            logger.error(f"Error executing task: {e}")
            # Remove task from the engine.tasks list after error
            self.tasks = [t for t in self.tasks if t.id != task.id]

    @property
    def agents_count(self) -> int:
        return len(self.agents)

    @property
    def tasks_count(self) -> int:
        return len(self.tasks)

    def execute_task_safely(self, task: Task) -> None:
        try:
            self.execute(task)
        except Exception as e:
            logger.error(f"Error executing task {task.id}: {e}")
            self.remove_task(task.id)
            raise TaskError(f"Error executing task {task.id}: {e}")

class MemoryGraph:
    def __init__(self) -> None:
        self.states = {}

    def update(self, task_id: str, state: Dict) -> None:
        self.states[task_id] = state

    def get_state(self, task_id: str) -> Dict:
        return self.states.get(task_id)