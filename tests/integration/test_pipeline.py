import unittest
from cli.main import main

class TestPipeline(unittest.TestCase):
    def test_pipeline(self) -> None:
        main()