from typing import List
import heapq

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sun = 0
        """
        想要完成有六个阶段项目(max_val)，至少需要五个其他项目(other_val)
        也就是说：other_val + 1 >= max_val
        """
        max_val = max(milestones)
        total_val = sum(milestones)
        other = total_val - max_val
        if max_val <= other:
            return total_val
        return total_val - other + 1

milestones = [10,1,10,12,13,15]
milestones = [49,1,2,3,51,100]
milestones = [1,2,3]
milestones = [5,2,1]
Solution().numberOfWeeks(milestones)