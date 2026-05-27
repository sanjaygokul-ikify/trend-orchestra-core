import argparse
from services.orchestrator import OrchestratorService

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent-id', required=True)
    parser.add_argument('--task-id', required=True)
    args = parser.parse_args()
    orchestrator = OrchestratorService()
    # Add agent and task logic here
    print('Orchestrator started')