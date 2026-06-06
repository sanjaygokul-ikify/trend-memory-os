from packages.core.memory_engine import MemoryEngine
from packages.utils.logging import Logger
from services.orchestrator import Orchestrator

def main() -> None:
    memory_graph = MemoryGraph([])
    memory_engine = MemoryEngine(memory_graph)
    orchestrator = Orchestrator(memory_engine)
    orchestrator.run()