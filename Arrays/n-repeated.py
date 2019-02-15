import operator


class Solution:
    def repeatedNTimes(self, array: 'List[int]'):
        check = dict()
        for i in range(len(array)):
            if array[i] in check:
                check[array[i]] += 1
            else:
                check[array[i]] = 1
        res = max(check.items(), key=operator.itemgetter(1))[0]
        print(res)


m = Solution()
m.repeatedNTimes([2, 1, 2, 5, 3, 2])
