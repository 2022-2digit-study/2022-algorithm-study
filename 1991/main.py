# (BOJ - 1991) 트리 순회 https://www.acmicpc.net/problem/1991

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self, size):
        self.nodes = [Node(chr(ascii_i)) for ascii_i in range(65, 65 + size)]
        self.root = self.nodes[0]

    @staticmethod
    def get_node_idx(alpha):
        return ord(alpha) - 65

    def insert_node(self, parent, left, right):
        if left != '.':
            self.nodes[self.get_node_idx(parent)].left_child = self.nodes[self.get_node_idx(left)]
        if right != '.':
            self.nodes[self.get_node_idx(parent)].right_child = self.nodes[self.get_node_idx(right)]


def xxx_order(xxx: str, node: Node) -> None:
    if not node:
        return
    if xxx.lower() == "pre":
        print(node.data, end="")  # 전위 순회
    xxx_order(xxx, node.left_child)
    if xxx.lower() == "in":
        print(node.data, end="")  # 중위 순회
    xxx_order(xxx, node.right_child)
    if xxx.lower() == "post":
        print(node.data, end="")


size = int(input())
t = Tree(size)

for _ in range(size):
    parent, lchild, rchild = sys.stdin.readline().split()
    t.insert_node(parent, lchild, rchild)

for xxx in ["pre", "in", "post"]:
    xxx_order(xxx=xxx, node=t.root)
    print()
