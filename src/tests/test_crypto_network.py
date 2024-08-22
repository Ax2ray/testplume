# tests/test_crypto_network.py
import unittest
from src.crypto_network import Node

class TestNode(unittest.TestCase):
    def test_connect(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.connect(node2)
        self.assertIn(node2, node1.connections)
        self.assertIn(node1, node2.connections)

if __name__ == "__main__":
    unittest.main()
