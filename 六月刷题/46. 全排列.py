from typing import List

class Solution:
    # https://leetcode.cn/problems/permutations/
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
         声明一个布尔数组 validator，validator 数组与nums长度相当
         validator 与 nums 索引元素相关联
         validator 中索引为 True 的表示对应的 nums 索引处已经排序完的，不可继续排序的
         validator 为 False 的索引 才表示对应的 nums 处允许排序
        """
        validator = [False] * len(nums)
        # 结果
        sun = []
        def compositor(single_group, level = 0):
            nonlocal validator
            nonlocal sun
            nonlocal nums
            # 验证当前“单种排序”中的全部元素是否全排序完成
            if all(validator):
                sun.append(list(single_group))
                return
            for i, n in enumerate(nums):
                # nums[i]已经在当前“单种排序”中排完序了，跳过nums[i]
                if validator[i]:
                    continue
                # 改变现场
                validator[i] = True
                single_group[level] = nums[i]
                compositor(single_group, level + 1)
                # 恢复现场
                validator[i] = False
                single_group[level] = 0
        # 单独的一种排序结果
        single_group = [0] * len(nums)
        compositor(single_group)
        return sun

nums = [1,2,3]
Solution().permute(nums)