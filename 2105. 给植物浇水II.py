from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        sun = 0
        left, right = 0, len(plants) - 1
        remain_water_A, remain_water_B = capacityA, capacityB
        while left <= right:
            # 双指针未相撞（俩人当前浇的植物不是同一株）
            if left < right:
                # Alice有足够的水浇灌第left株植物
                if remain_water_A >= plants[left]:
                    remain_water_A -= plants[left]
                    left += 1
                else:
                    # Alice没有足够的水浇灌第left株植物，需要重新灌水。
                    sun += 1
                    remain_water_A = capacityA
                    # 为了保证Alice和Bob的同步浇水，重新打完水之后立马前进
                    remain_water_A -= plants[left]
                    left += 1

                # Bob有足够多的水浇灌第right株植物。
                if remain_water_B >= plants[right]:
                    remain_water_B -= plants[right]
                    right -= 1
                else:
                    # Bob没有足够多的水浇灌第right株植物，需要重新灌水。
                    sun += 1
                    remain_water_B = capacityB
                    # 为了保证Alice和Bob的同步浇水，重新打完水之后立马前进
                    remain_water_B -= plants[right]
                    right -= 1
            else:
                # lice 和 Bob 到达同一株植物
                if remain_water_A < plants[left] and remain_water_B < plants[right]:
                    sun += 1
                break
        return sun