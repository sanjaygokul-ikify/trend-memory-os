from packages.core.memory_engine import MemoryEngine
from packages.utils.logging import Logger

class Orchestrator:
    def __init__(self, memory_engine: MemoryEngine):
        self.memory_engine = memory_engine
        self.logger = Logger(__name__)

    def run(self) -> None:
        try:
            self.memory_engine.ingest_raw_data([b'data'])
        except Exception as e:
            self.logger.error(f'Error running orchestrator: {e}')