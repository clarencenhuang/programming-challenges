import math
from functools import lru_cache


def get_min_cuts(s):

    @lru_cache(None)
    def is_palindrome(i, j):
        if i == j:
            return True
        start_eq_end = s[i] == s[j]
        if start_eq_end and j == i + 1:
            return True
        elif start_eq_end and is_palindrome(i+1, j-1):
            return True
        return False

    @lru_cache(None)
    def min_cut(i, j):
        if is_palindrome(i, j):
            return 0
        n_min_cuts = math.inf
        for m in range(i, j):
            n_min_cuts = min(n_min_cuts, 1 + min_cut(i, m) + min_cut(m + 1, j))
        return n_min_cuts

    return min_cut(0, len(s) - 1)


def get_min_cuts_dp(s):
    dp_palin = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]
    dp_cuts = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

    for l in range(1, len(s) + 1):
        for i in range(1, len(s) + 1):
            j = i + l - 1
            if j > len(s):
                break
            #print(i, j)
            # update dp palin
            i_j_letters_same = s[i-1] == s[j-1]
            if i == j or (i_j_letters_same and j == i + 1):
                dp_palin[i][j] = True
            else:
                if i_j_letters_same:
                    dp_palin[i][j] = dp_palin[i+1][j-1]

            # update cuts
            if dp_palin[i][j]:
                dp_cuts[i][j] = 0
            else:
                n_min_cuts = math.inf
                for m in range(i, j):
                    n_min_cuts = min(n_min_cuts, 1 + dp_cuts[i][m] + dp_cuts[m+1][j])
                dp_cuts[i][j] = n_min_cuts

    return dp_cuts[1][len(s)]





if __name__ == '__main__':
    #print(get_min_cuts("aabbbccccccd"))
    print(get_min_cuts_dp("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))