#nex = curr[:i] + curr[j] + curr[i + 1:j] + curr[i] + curr[j + 1:]
def kSimilarity(A: str, B: str) -> int:

    depth_cache = dict()
    len_str = len(A)
    best_k = 100000

    def dfs(curr, depth=0):
        nonlocal best_k
        if curr in depth_cache:
            if depth > depth_cache[curr]:
                return
        depth_cache[curr] = depth
        if depth >= best_k:
            return
        if curr == B:
            if depth < best_k:
                best_k = depth
                print(depth)
        for i in range(depth, len_str):
            if curr[i] != B[i]:
                for j in range(i+1, len_str):
                    if curr[j] == B[i]:
                        nex = curr[:i] + curr[j] + curr[i + 1:j] + curr[i] + curr[j + 1:]
                        dfs(nex, depth+1)
                break
    dfs(A)
    return best_k





if __name__ == '__main__':
    A = "abccaacceecdeea"
    B = "bcaacceeccdeaae"
    #A = "bccaba"
    #B = "abacbc"
    print(kSimilarity(A, B))
