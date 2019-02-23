"""
@author: Priyanka Punjabi
"""
def solution(S):
    v = int(S, 2)
    count = 0
    while v != 0:
        if v % 2 == 0:
            v = v / 2
        else:
            v = v - 1
        count += 1
    return count


print(solution('011100'))
