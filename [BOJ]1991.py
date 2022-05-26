# 백준 - https://www.acmicpc.net/problem/1991

import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(node):
    print(node.data, end='')
    if (left := node.left) != '.':
        preorder(tree[left])
    if (right := node.right) != '.':
        preorder(tree[right])


def inorder(node):
    if (left := node.left) != '.':
        inorder(tree[left])
    print(node.data, end='')
    if (right := node.right) != '.':
        inorder(tree[right])


def postorder(node):
    if (left := node.left) != '.':
        postorder(tree[left])
    if (right := node.right) != '.':
        postorder(tree[right])
    print(node.data, end='')


N = int(sys.stdin.readline().strip())
tree = dict()

for _ in range(N):
    parents, left_child, right_child = sys.stdin.readline().split()
    tree[parents] = Node(parents, left_child, right_child)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
