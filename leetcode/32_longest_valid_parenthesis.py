import functools


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def longest_seq_ending_at(idx):
            if idx < 0:
                return 0
            if s[idx] == ')' and idx > 0:
                if s[idx - 1] == '(':
                    return longest_seq_ending_at(idx - 2) + 2 # ()()
                elif s[idx - 1] == ')':
                    seqlen = longest_seq_ending_at(idx - 1) # ()(())
                    if seqlen > 0 and idx - seqlen - 1 >= 0 and s[idx - seqlen - 1] == '(':
                        return seqlen + 2 + longest_seq_ending_at(idx - seqlen - 2)
            return 0

        max_len = 0
        for i in range(len(s)):
            le = longest_seq_ending_at(i)
            #print(f"{i}: {le}")
            max_len = max(max_len, le)
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()))())("))