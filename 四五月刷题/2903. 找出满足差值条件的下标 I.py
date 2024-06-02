from typing import List

class Solution:
    def findIndices2(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        sun = [-1, -1]
        left,right = 0, 0
        validator = False
        while right < len(nums):
            while right < len(nums):
                if abs(left - right) >= indexDifference and abs(nums[left] - nums[right]) >= valueDifference:
                    sun = [left, right]
                    validator = True
                    break
                right += 1
            if validator:
                break
            # 更新左节点
            left += 1
            right = left
        return sun
