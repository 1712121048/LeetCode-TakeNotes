import copy
import math
import heapq
from typing import List


class Solution:
    # 超时（超时并不代表代码不够优雅）
    def totalCost2(self, costs: List[int], k: int, candidates: int) -> int:
        result = 0
        def direct_data(array):
            res = 0
            if candidates * 2 >= len(array):
                array.sort()
                res = sum(array[:k])
            return res
        result = direct_data(costs)

        # 如果candidates*2>=costs.length则说明costs里面全部都是候选人
        if result > 0:
            return result
        else:
            # 否则的话则说明需要在候选人中挑选

            costs_len = len(costs)
            # 堆化，小根堆（带索引），自下而上建堆法。
            def repair_heap(rootlet_heap):
                for i in range(len(rootlet_heap) - 1, -1, -1):
                    parent_idx = int(math.floor(i - 1)/2)
                    if parent_idx < 0:
                        break
                    curr = rootlet_heap[i]
                    parent = rootlet_heap[parent_idx]
                    if curr < parent:
                        rootlet_heap[parent_idx] = curr
                        rootlet_heap[i] = parent
                return rootlet_heap

            # 雇佣k名工人
            before = [(n, i) for i, n in enumerate(costs[:candidates])]
            after = [(n, i) for i, n in enumerate(costs[-candidates:], costs_len - candidates)]
            while k > 0:
                """
                （v,i）：v是costs的值，i是costs里面的索引
                costs = [5, 6, 1,   2, 6,   2, 9, 1]
                heap = [(5, 0),(6, 1),(1, 2),  (2, 5),(9, 6),(1, 7)]
                """
                if candidates * 2 >= costs_len:
                    costs.sort()
                    result += sum(costs[:k])
                    break

                # 更新before和after内的元素 （改为下面的方式，通过判断更新before和after内的元素。或许感觉下面的效率更高吧）
                # before = [(n, i) for i, n in enumerate(costs[:candidates])]
                # after = [(n, i) for i, n in enumerate(costs[-candidates:], len(costs) - candidates)]

                sun = before+after
                # 小根堆化列表
                heap = repair_heap(sun) # 小根堆
                # 代价最小的候选人
                min_data = heap[0]
                del_idx = min_data[1]

                # region 更新before和after内的元素
                # 前半部分
                if del_idx < candidates:
                    last_idx = before[-1][1]
                    before.remove(min_data)
                    if last_idx + 1 < costs_len:
                        # 添加候选人
                        el_tpe = (costs[last_idx + 1], last_idx + 1)
                        before.append(el_tpe)
                        # 更新索引
                        before = before[:del_idx] + list(map(lambda x: (x[0], x[1] - 1), before[del_idx:]))
                        after = list(map(lambda x: (x[0], x[1] - 1), after))
                else:
                    first_idx = after[0][1]
                    a_del_idx = after.index(min_data)
                    after.remove(min_data)
                    if first_idx - 1 > 0:
                        # 更新索引
                        after = after[:a_del_idx] + list(map(lambda x: (x[0], x[1] - 1), after[a_del_idx:]))
                        # 添加候选人
                        el_tpe = (costs[first_idx - 1], first_idx - 1)
                        after.insert(0, el_tpe)
                # endregion

                result += min_data[0]
                costs.pop(del_idx)
                k -= 1
                costs_len -= 1
        return result

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        c_len = len(costs)
        # 双指针
        l, r = candidates, c_len - 1 - candidates
        # 双指针是否对撞
        if l > r:
            # 如果指针对撞则说明全部都是候选人
            costs.sort()
            res = sum(costs[:k])
        if res == 0:
            # init before/after
            before, after = costs[:candidates], costs[-candidates:]
            heapq.heapify(before)
            heapq.heapify(after)
            # [5,6,1,2,6,1,9,2,8]
            while k > 0:
                # 双指针是否对撞
                if l > r:
                    # 如果指针对撞则说明列表中全部都是候选人
                    sun = before + after
                    sun.sort()
                    res += sum(sun[:k])
                    break
                b_min, a_min = before[0], after[0]
                if b_min <= a_min:
                    min_val = heapq.heapreplace(before, costs[l])
                    res += min_val
                    # heapq.heapify(before)
                    l += 1
                else:
                    min_val = heapq.heapreplace(after, costs[r])
                    res += min_val
                    # heapq.heapify(after)
                    r -= 1
                k -= 1
        return res


costs = [5, 6, 1,   2, 6,   1, 9, 2]
k = 5
candidates = 3

costs = [1,2,4,1]
k = 3
candidates = 3

costs = [5,6,1,  2,6,1,  9,2,8]
k = 2
candidates = 3

costs = [5, 1, 6,   2, 6,   2, 1, 6]
k = 3
candidates = 3

# costs = [5,6,3,2,1,1]
# k = 5
# candidates = 2

# costs = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# k = 5
# candidates = 3

costs = [5,6,1,2,6,1,9,2,8]
k = 2
candidates = 3
Solution().totalCost(costs,k,candidates)