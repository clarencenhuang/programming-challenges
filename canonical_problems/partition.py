# https://interviewing.io/recordings/CSharp-Microsoft-5

arr = [4, 5, 3, 2, 1, 0]

#
# [low|mid|hi]
#
# mid
# hi

k = 3
mid, hi = 0, 0
for i,n in enumerate(arr):
    if n < 3:
        mid += 1
        hi += 1
    if n == 3:
        pass
