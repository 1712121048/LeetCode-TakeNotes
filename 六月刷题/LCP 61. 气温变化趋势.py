from typing import List

class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        def get_fLag(nums, idx):
            if nums[idx] == nums[idx - 1]:
                return 0
            elif nums[idx] > nums[idx - 1]:
                return 1
            return -1
        sun = 0
        record = 0
        # 上次 temperatureA 和 temperatureB 相同的趋势状态
        last_flag = -2
        for i in range(1, len(temperatureA)):
            A_flag, B_flag = get_fLag(temperatureA, i), get_fLag(temperatureB, i)
            if A_flag == B_flag:
                last_flag = A_flag if last_flag == -2 else last_flag
                if last_flag == A_flag or 1 == 1:
                    record = (record == 0) * 2 + (record > 0) * (record + 1)
                else:
                    record = 0
            else:
                record = 0
            sun = max(sun, record)
        return sun


temperatureA = [ 5,10,16,-6,15,11, 3]
temperatureB = [16,22,23,23,25,3,-16]
# temperatureA = [1,2,1,2,1]
# temperatureB = [1,2,1,2,1]
Solution().temperatureTrend(temperatureA, temperatureB)