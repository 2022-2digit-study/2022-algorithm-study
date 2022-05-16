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


def pre_order(node: Node):
    if not node:
        return
    print(node.data, end="")  # 전위 순회
    pre_order(node.left_child)
    pre_order(node.right_child)


def in_order(node: Node):
    if not node:
        return
    in_order(node.left_child)
    print(node.data, end="")  # 중위 순회
    in_order(node.right_child)


def post_order(node: Node):
    if not node:
        return
    post_order(node.left_child)
    post_order(node.right_child)
    print(node.data, end="")  # 후위 순회


size = int(input())
t = Tree(size)

for _ in range(size):
    parent, lchild, rchild = sys.stdin.readline().split()
    t.insert_node(parent, lchild, rchild)

pre_order(t.root)
print()
in_order(t.root)
print()
post_order(t.root)
print()
