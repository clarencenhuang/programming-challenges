#https://www.geeksforgeeks.org/build-original-array-from-the-given-sub-sequences/
from collections import defaultdict


def get_original_sequence(subseqs):
    graph = defaultdict(set)
    nodes = set()
    for subseq in subseqs:
        for i in range(len(subseq)):
            nodes.add(subseq[i])
            if i < len(subseq) - 1:
                graph[subseq[i]].add(subseq[i + 1])

    visited = set()
    explored = []

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

    return list(reversed(explored))



if __name__ == '__main__':
     print(get_original_sequence([[1, 2, 3], [1, 2], [3, 4], [5, 2], [0, 5, 4]]))
