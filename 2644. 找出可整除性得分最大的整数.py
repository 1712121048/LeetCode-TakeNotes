from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        sun = min(divisors)
        max_multiple = 0
        divisors_set = set(divisors)
        for n in divisors_set:
            n_max_multiple = 0
            for num in nums:
                if num % n == 0:
                    n_max_multiple += 1
            if n_max_multiple > max_multiple or (n_max_multiple == max_multiple and n < sun):
                max_multiple = max(n_max_multiple,max_multiple)
                sun = n
        return sun

nums = [20,14,21,10]
divisors = [5,7,5]
# nums = [12]
# divisors = [10,6]
Solution().maxDivScore(nums,divisors)