from functools import lru_cache

def shortet_common_supersequence(str1, str2):

    @lru_cache(None)
    def scs(i1, i2):
        if i1 == 0 and i2 == 0:
            return 0
        elif i1 == 0:
            return i2
        elif i2 == 0:
            return i1

        if str1[i1-1] == str2[i2-1]:
            return 1 + scs(i1 - 1, i2 - 1)
        else:
            return 1 + min(scs(i1, i2-1), scs(i1-1, i2))

    i1, i2 = len(str1), len(str2)
    final_str = ''
    while i1 > 0 or i2 > 0:
        if i1 == 0:
            final_str += str2[:i2]
            i2 = 0
        elif i2 == 0:
            final_str += str1[:i1]
            i1 = 0
        elif str1[i1-1] == str2[i2-1]:
            final_str += str1[i1-1]
            #print("same", str2[i2 - 1])
            i1 -= 1
            i2 -= 1
        elif scs(i1, i2) == scs(i1, i2-1) + 1:
            final_str += str2[i2-1]
            #print("i2", str2[i2-1])
            i2 -= 1
        elif scs(i1, i2) == scs(i1-1, i2) + 1:
            final_str += str1[i1-1]
            #print("i1", str1[i1-1])
            i1 -= 1
        else:
            raise Exception('aa')
    return final_str[::-1]

if __name__ == '__main__':
    print(shortet_common_supersequence('abac', 'cab'))
