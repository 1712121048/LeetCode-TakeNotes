class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        full_sort = self.closure_full_ranking(n, k)
        result = full_sort()
        return result[-1]

    def closure_full_ranking(self, n ,k):
        validator = [True]*n
        nums = list(range(1,n + 1))
        record = []
        def full_sort(prefix = ""):
            nonlocal validator, nums, record
            if k > len(record):
                for n in nums: #枚举所有可能
                    if not validator[n - 1]: #判断是否合法
                        continue
                    validator[n - 1] = False #改变现场
                    if True not in validator:
                        record.append(prefix + str(n)) #执行目标
                    else:
                        full_sort(prefix + str(n)) #递归调用
                    validator[n - 1] = True #恢复现场
            return record
        return full_sort

Solution().getPermutation(4,9,)

