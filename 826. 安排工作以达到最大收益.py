import heapq
import bisect
import numpy
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sun = 0
        # 对能力排序
        worker.sort()
        # 排序difficulty。difficulty的排序会带动profit一并调整顺序
        # 使用 zip 将 difficulty 和 profit 组合在一起
        combined = zip(difficulty, profit)

        # 对组合后的元素按 difficulty 进行排序
        sorted_combined = sorted(combined, key=lambda x: x[0])

        # 分离排序后的 difficulty 和 profit
        difficulty = [item[0] for item in sorted_combined]
        profit = [item[1] for item in sorted_combined]

        expand = []
        i = 0
        into_heapq_idx = 0
        """
        [001, 002, 003, 006, 008, 008, 008, 010]
        [200, 010, 020, 030, 060, 055, 900, 050]
        [004, 005, 006, 007, 009]
        """
        while i < len(worker):
            end = bisect.bisect_right(difficulty, worker[i])
            for n in range(into_heapq_idx, end):
                heapq.heappush(expand, -profit[n])
            i += 1
            if len(expand) == 0:
                # 所有任务worker[i]没有一件能干得了
                continue
            sun += expand[0]
            into_heapq_idx = end
        return sun * -1

difficulty = [3, 2, 8, 6, 8, 1, 10, 8]
profit = [20, 10, 60, 30, 55, 200, 50, 900]
worker = [4, 5, 6, 7, 9]

# difficulty = [85,47,57]
# profit = [24,66,99]
# worker = [40,25,25]
Solution().maxProfitAssignment(difficulty,profit,worker)