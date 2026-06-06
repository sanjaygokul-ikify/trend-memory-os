import unittest
from packages.core.memory_engine import MemoryEngine, MemoryGraph
from packages.core.types import MemoryNode, Fact

class TestCore(unittest.TestCase):
    def test_ingest_raw_data(self) -> None:
        memory_graph = MemoryGraph([])
        memory_engine = MemoryEngine(memory_graph)
        memory_engine.ingest_raw_data([b'data'])
        self.assertEqual(len(memory_graph.nodes), 1)

    def test_extract_facts(self) -> None:
        memory_graph = MemoryGraph([MemoryNode([b'data'])])
        memory_engine = MemoryEngine(memory_graph)
        facts = memory_engine.extract_facts(memory_graph.nodes[0])
        self.assertEqual(facts, [])