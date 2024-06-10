from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        sun = 0
        standard = nums[0] + nums[1]
        while len(nums) >= 2:
            first = nums.pop(0)
            second = nums.pop(0)
            if standard != first + second:
                break
            sun += 1
        return sun