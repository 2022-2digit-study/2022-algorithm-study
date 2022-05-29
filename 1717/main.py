import sys


def union(elem1, elem2):
    if elem1 != elem2:
        parents[find(elem2, True)] = find(elem1, True)


def find(elem, initialize: bool):
    if parents[elem] == elem:
        return elem
    elem_parent = find(parents[elem], initialize)
    if initialize:
        parents[elem] = elem_parent
    return elem_parent


n, m = map(int, sys.stdin.readline().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command:
        if find(a, False) == find(b, False):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
