

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        so_far = []
        for prefixes in zip(*strs):
            if len(set(prefixes)) > 1:
                break
            else:
                so_far.append(prefixes[0])
        return ''.join(so_far)


if __name__ == '__main__':
    s = Solution()
    s.longestCommonPrefix(["ABCD","ABEF","ACEF"])