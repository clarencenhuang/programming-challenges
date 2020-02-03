from typing import List
from collections import defaultdict, deque

def build_graph(word_list):
    word_list = set(word_list)
    word_groups = defaultdict(set)
    graph = defaultdict(set)

    for w in word_list:
        for i, l in enumerate(w):
            key = w[:i] + '*' + w[i+1:]
            word_groups[key].add(w)

    for values in word_groups.values():
        for w in values:
            graph[w] |= values - {w}

    return graph

def bfs(begin_w, end_w, graph):
    q = deque([(begin_w, 1)])
    history_set = set()
    while q:
        w, steps = q.popleft()
        if w == end_w:
            return steps
        for w1 in graph[w]:
            if w1 not in history_set:
                history_set.add(w1)
                q.append((w1, steps + 1))
    return 0



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = build_graph(wordList + [beginWord])
        return bfs(beginWord, endWord, graph)

if __name__ == '__main__':
    s = Solution()
    a = "hit"
    b = "cog"
    c = ["hot", "dot", "dog", "lot", "log"]
    print(s.ladderLength(a, b, c))
