'''
    @author: Priyanka Punjabi
'''

class Solution:
    def checkPossibility(self, A):
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if p is not None:
                    return False
                p = i
        return True

m = Solution()
a = [1, 2, 3, 4, 8, 9, 6]
print(m.checkPossibility(a))
b = [1, 2, 3, 4, 8, 7, 6]
print(m.checkPossibility(b))
