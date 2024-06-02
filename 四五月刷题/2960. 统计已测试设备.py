from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        # 不用模拟，用不着真的去模拟将[i+1,n-1]的元素全部减去一
        sun = 0 # 结果（i处应该减去的值）
        for i in batteryPercentages:
            if i - sun > 0:
                sun += 1
        return sun