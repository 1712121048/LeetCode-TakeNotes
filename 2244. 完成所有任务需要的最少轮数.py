import collections
import math
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        sun = 0
        counter = collections.Counter(tasks)
        if counter.most_common()[-1][1] == 1:
            return -1
        """
        任务数%3会有三种情况。
        想让获取最少轮数就优先使用3。
        只要不存在出现次数等于1的数值，则必定可以完成。
        1、0：直接被3整除。
        2、1：最后两轮由2完成。
        3、2：最后一轮由完成。
        """
        tasks_nums = list(dict(counter).values())
        while len(tasks_nums) > 0:
            num = tasks_nums.pop()
            if num == 2 or num == 3:
                sun += 1
            elif num % 3 == 0:
                sun += num / 3
            elif num % 3 == 1:
                num -= 4
                sun += int(num / 3)
                sun += 2
            elif num % 3 == 2:
                num -= 2
                sun += int(num / 3)
                sun += 1
        return sun

minMovesToMakePalindrome = [2,2,3,3,2,4,4,4,4,4]
Solution().minimumRounds(minMovesToMakePalindrome)