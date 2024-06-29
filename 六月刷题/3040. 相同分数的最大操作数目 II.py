from functools import cache
from typing import List
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        # 三种模式
        enum_flag = 0, 1, 2
        @cache
        def dfs(start, end, ask) -> int:
            nonlocal nums
            nonlocal enum_flag
            curr_nums = nums[start:end]
            if len(curr_nums) == 0:
                return 0
            curr = 0
            for f in enum_flag:
                # 被分割后的数组
                # cache 不支持 dfs_nums = [] 不可哈希类型
                start_dfs, end_dfs = start, end
                # 标准值
                dfs_ask = 0
                # 状态
                flag = False
                if len(curr_nums) == 1:
                    """
                    一次性必须干掉两个，如果出现一个则中断
                    【选择 nums 中第一个和最后一个元素并且删除它们】这个句也是删除两个，最后一个和第一个不能为同一个元素
                    """
                    # if curr_nums[0] == ask:
                    #     start_dfs = end_dfs
                    #     flag = True
                    #     curr = 1
                    #     break
                    break
                elif f == 0 and not flag:
                    # dfs_nums = curr_nums[2:]
                    start_dfs += 2
                    dfs_ask = curr_nums[0] + curr_nums[1]
                    if dfs_ask == ask:
                        flag = True
                elif f == 1:
                    # dfs_nums = curr_nums[:len(curr_nums) - 2]
                    end_dfs += -2
                    dfs_ask = curr_nums[-1] + curr_nums[-2]
                    if dfs_ask == ask:
                        flag = True
                else:
                    # dfs_nums = curr_nums[1:len(curr_nums) - 1]
                    start_dfs += 1
                    end_dfs += -1
                    dfs_ask = curr_nums[0] + curr_nums[-1]
                    if dfs_ask == ask:
                        flag = True
                if flag:
                    res = dfs(start_dfs, end_dfs, dfs_ask)
                    curr = max(1 + res, curr)
            return curr

        sun = 0
        for f in enum_flag:
            ask = 0
            # cache 不支持 dfs_nums = [] 不可哈希类型
            # dfs_nums = []
            start_dfs, end_dfs = 0, len(nums)
            if f == 0:
                # dfs_nums = nums[2:]
                ask = nums[0] + nums[1]
                start_dfs += 2
            elif f == 1:
                # dfs_nums = nums[:len(nums) - 2]
                ask = nums[-1] + nums[-2]
                end_dfs -= 2
            else:
                # dfs_nums = nums[1:len(nums) - 1]
                ask = nums[0] + nums[-1]
                start_dfs += 1
                end_dfs -= 1
            sun = max(dfs(start_dfs, end_dfs, ask) + 1, sun)
        return sun

nums = [1,1,1,1,2]
Solution().maxOperations(nums)