import bisect
from typing import List
from math import inf
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 已经更新了的坐标集合
        idxs = set()
        # 结果
        sun = [-1] * len(nums)
        # 单调栈
        stack = []
        # 因为 nums 是循环数组，所以枚举 nums 的两倍即可
        for i in range(len(nums) * 2 + 1):
            # nums 的索引
            idx = i % len(nums)
            # 保持栈的有序性，将 nums[idx] 插入有序位置
            insert_idx = len(stack) - bisect.bisect_right(stack[::-1], nums[idx])
            # 如果 insert_idx < len(stack) 则说明栈中存在比 nums[idx] 小的值，根据题意，要将那些 [没有被更新过的]、[idx 左侧的]、[比 nums[idx] 小的] 进行更新
            if insert_idx < len(stack):
                # 从 当前(i) 开始往左侧更新，所以反转列表
                ary = [n for n in range(i)][::-1]
                # 往左侧变量
                for j in ary:
                    # 左侧的 index
                    index = j % len(nums)
                    # 粗剪枝，如果左侧出现了比 nums[idx] 更大的值，则不用更新了，因为他们肯定被 这个更大的值所更新了（如果这个更大值都无法更新那些为 -1 的值，说明那些为 -1 的值比 nums[index] 还大，如果 -1 的值比 nums[index] 都大的话，那 nums[idx] 更是白搭，剪枝）
                    if nums[index] >= nums[idx]:
                        break
                    # 对那些符合规矩且没有被更新过的 -1 进行更新
                    elif sun[index] == -1 and not index in idxs:
                        sun[index] = nums[idx]
                        idxs.add(index)
            # 更新单调栈，将栈中比 nums[idx] 小的全部干掉
            stack = stack[:insert_idx]
            # 入栈
            stack.append(nums[idx])
        return sun

nums = [5,3,2,4,3]
nums = [1,2,1]
nums = [-1,-2,-1,1]
Solution().nextGreaterElements(nums)