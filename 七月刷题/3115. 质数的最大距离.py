from typing import List
import math
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        # 快速判断质数
        def prime(n):
            if n == 1:
                return False
            elif n == 2 or n == 3:
                return True
            if n % 6 != 1 and n % 6 != 5: # 不在 6 的倍数两侧的一定不是质数
                return False
            for i in range(5, math.floor(math.sqrt(n)) + 1, 6): # 在 6 的倍数两侧的也可能不是质数
                if n % i == 0 or n % (i + 2) == 0: # 排除所有剩下的就是质数
                    return False
            return True
        first, last = math.inf, -math.inf
        for i, n in enumerate(nums):
            if prime(n):
                first = min(i, first)
                last = max(i, last)

        sun = 0
        if first > last:
            # 一个质数也没有
            return sun
        sun = last - first
        return sun

nums = [1,7]
Solution().maximumPrimeDifference(nums)