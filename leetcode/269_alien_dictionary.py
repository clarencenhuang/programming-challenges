# https://www.lintcode.com/problem/alien-dictionary/description
# TOPOLOGICAL SORT!!!!
from collections import defaultdict


def alien_dictionary(words):
    graph = defaultdict(set)
    nodes = set()
    for i in range(1, len(words)):
        for l1, l2 in zip(words[i-1], words[i]):
            if l1 != l2:
                graph[l1].add(l2)
                nodes.add(l1)
                nodes.add(l2)
                break
    explored = []
    visited = set()

    def explore(n):
        if n in visited:
            return
        visited.add(n)
        for child in graph[n]:
            explore(child)
        explored.append(n)

    for node in nodes:
        if node not in visited:
            explore(node)

    return ''.join(reversed(explored))

if __name__ == '__main__':
    assert alien_dictionary(["wrt","wrf","er","ett","rftt"]) == 'wertf'
    assert alien_dictionary(["z","x"]) == 'zx'
