from dataclasses import dataclass
from typing import List, Dict

@dataclass
class MemoryNode:
    data: List[bytes]

@dataclass
class MemoryGraph:
    nodes: List[MemoryNode]

    def add_node(self, node: MemoryNode) -> None:
        self.nodes.append(node)

@dataclass
class Fact:
    key: str
    value: str

@dataclass
class Context:
    facts: List[Fact]