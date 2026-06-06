import unittest
from packages.core.memory_engine import MemoryEngine
from packages.core.types import MemoryGraph

class TestRuntime(unittest.TestCase):
    def test_memory_engine(self) -> None:
        memory_graph = MemoryGraph([])
        memory_engine = MemoryEngine(memory_graph)
        memory_engine.ingest_raw_data([b'data'])