

tc = [None, False, False, False, True, True]

class SVNRepo:
   @classmethod
   def isBadVersion(cls, id):
    return tc[id]

def fbv(v):
    l, r  = 1, v
    while r > l:
        m = l + (r - l) // 2
        if SVNRepo.isBadVersion(m):
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    print(fbv(5))
