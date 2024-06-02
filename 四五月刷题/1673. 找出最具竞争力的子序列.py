from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        [2,4,3,3,5,1,9,6]
        
        [4,2]
        [3,4,2]
        [3,2]
        [3,3,2]
        [5,3,3,2]
        [1,5,3,3,2]
        [1,3,3,2]
        [1,3,2]
        [9,1,3,2]
        [6,9,1,3,2]

        [1,0,1,1,0,1,0,1,0]
        """
        if len(nums) == k:
            return nums
        sun = []
        stack = []
        first = nums[0]
        nums_residual, stack_len = len(nums), 0
        while len(nums) > 0:
            stack.insert(0, nums.pop(0))
            nums_residual -= 1
            stack_len += 1

            # nums剩下的大于k空下的，说明k还有资格挑选更好的货物
            while nums_residual > k - stack_len and stack_len > 1:
                if stack[1] > stack[0]:
                    stack.pop(1)
                    stack_len -= 1
                else:
                    break
        if len(stack) < k:
            stack.append(first)
        sun = stack[::-1][:k]
        return sun

nums = [2,4,1,3,5,4,9,6]
k = 4
# nums = [3,5]
# k = 1
# nums = [5,3]
# k = 2
# nums = [1,2,3,5,0,1,0,1,1,2,1,5]
# k = 3
# nums = [1,0,1,1,0,1,0,1,0]
# k = 3
Solution().mostCompetitive(nums, k)