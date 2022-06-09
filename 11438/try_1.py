import sys


# 시간 초과
class Node:
    def __init__(self, data, depth, parent=None):
        self.data = data
        self.parent = parent
        self.depth = depth


class Tree:
    def __init__(self):
        self.root = Node(1, 1)
        self.nodes = {1: self.root}

    @staticmethod
    def find_depth_parent(node, depth):
        tmp_node = node
        while tmp_node.depth != depth:
            tmp_node = tmp_node.parent
        return tmp_node

    def insert_node(self, parent, data):
        if not self.nodes.get(parent):
            parent, data = data, parent
        parent = self.nodes.get(parent)
        self.nodes[data] = Node(data, parent.depth + 1, parent)

    def get_lca(self, node1_data, node2_data):
        node1 = self.nodes.get(node1_data)
        node2 = self.nodes.get(node2_data)
        max_depth_node = max(node1, node2, key=lambda x: x.depth)
        min_depth_node = min(node2, node1, key=lambda x: x.depth)

        max_depth_node = self.find_depth_parent(max_depth_node, min_depth_node.depth)

        while max_depth_node.data != min_depth_node.data:
            max_depth_node = max_depth_node.parent
            min_depth_node = min_depth_node.parent
        return max_depth_node.data


tree = Tree()
N = int(sys.stdin.readline())
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree.insert_node(a, b)

M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(tree.get_lca(a, b))
