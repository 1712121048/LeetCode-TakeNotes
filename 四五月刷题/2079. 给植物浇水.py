from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        # 初始水量是满的
        remain_water = capacity
        i, plants_len = 0, len(plants)
        while i < plants_len:
            if remain_water >= plants[i]:
                # 增加步数
                res += 1
                # 浇水
                remain_water -= plants[i]
                i += 1
            else:
                # 从i处到河边紧接着又返回i处的步数
                step_num = i * 2
                # 加入步数
                res += step_num
                # 重新装水
                remain_water = capacity
        return res