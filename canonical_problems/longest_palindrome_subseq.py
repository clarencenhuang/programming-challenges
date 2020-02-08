


def longest_palindrome_subseq(s):

    def dp(i, j):
        ends_eq = s[i] == s[j]
        if i == j or ends_eq and j == i + 1:
            return j - i + 1
        if ends_eq:
            return 2 + dp(i+1, j-1)
        else:
            return max(dp(i+1, j), dp(i, j-1))

