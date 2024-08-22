# src/crypto_network.py
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connections = []

    def connect(self, other_node):
        if other_node not in self.connections:
            self.connections.append(other_node)
            other_node.connections.append(self)

def main():
    node1 = Node(1)
    node2 = Node(2)
    node1.connect(node2)
    print(f'Node {node1.node_id} connected to {[n.node_id for n in node1.connections]}')

if __name__ == "__main__":
    main()
