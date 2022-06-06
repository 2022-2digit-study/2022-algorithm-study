# import sys
#
#
# class Node:
#     def __init__(self, data, depth, parent=None):
#         self.
#         data = data
#         self.parent = parent
#         self.depth = depth
#
#
# class Tree:
#     def __init__(self):
#         self.root = Node(1, 1)
#         self.nodes = [self.root]
#
#     def find_node(self, data):
#         for n_i in range(len(self.nodes)):
#             if self.nodes[n_i].data == data:
#                 return n_i
#         return -1
#
#     @staticmethod
#     def find_depth_parent(node, depth):
#         tmp_node = node
#         while tmp_node.depth != depth:
#             tmp_node = tmp_node.parent
#         return tmp_node
#
#     def insert_node(self, parent, data):
#         if self.find_node(parent) == -1:
#             parent, data = data, parent
#         parent = self.nodes[self.find_node(parent)]
#         new_node = Node(data, parent.depth + 1, parent)
#         self.nodes.append(new_node)
#
#     def get_lca(self, node1_data, node2_data):
#         node1 = self.nodes[self.find_node(node1_data)]
#         node2 = self.nodes[self.find_node(node2_data)]
#         max_depth_node = max(node1, node2, key=lambda x: x.depth)
#         min_depth_node = min(node2, node1, key=lambda x: x.depth)
#
#         max_depth_node = self.find_depth_parent(max_depth_node, min_depth_node.depth)
#
#         while max_depth_node.data != min_depth_node.data:
#             max_depth_node = max_depth_node.parent
#             min_depth_node = min_depth_node.parent
#         return max_depth_node.data
#
#
# tree = Tree()
# N = int(sys.stdin.readline())
# for _ in range(N - 1):
#     a, b = map(int, sys.stdin.readline().split())
#     tree.insert_node(a, b)
#
# M = int(sys.stdin.readline())
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     print(tree.get_lca(a, b))
# 시간 초과..

#