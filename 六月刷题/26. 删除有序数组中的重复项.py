import math
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 因为集合是无序的，所以不要使用集合去重 return list(set(nums))
        if len(nums) == 1:
            return 1

        left, right = 0, 1
        while right < len(nums):
            if nums[right] == nums[left]:
                nums.pop(left)
            else:
                left = right
                right += 1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)
