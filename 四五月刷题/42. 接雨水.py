from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_idx = 0
        left_val = height[left_idx]
        graph_len = 1 # 一基索引。图形长度
        result = 0
        for curr_idx, curr_val in enumerate(height):
            """
            当右指针大于等于左指针对雨水进行计算
            
            空白：(右指针*矩形长度)-(左指针*矩形长度)==0?(右指针*矩形长度)-(左指针*矩形长度):(右指针*矩形长度)-(左指针*矩形长度)-(右指针-左指针)。
            水：(右指针*矩形长度)-全部的砖-空白
            """
            if curr_val >= left_val:
                # 计算雨水面积
                max_height = max(left_val, curr_val) # 最大矩形高度
                min_height = min(left_val, curr_val) # 最小矩形高度
                extra = 0 if max_height == min_height else max_height - min_height # 额外部分
                blank = (max_height * graph_len) - (min_height * graph_len) - extra # 空白格子
                all_brick = sum(height[left_idx: left_idx + graph_len]) # 全部的砖
                water = (max_height * graph_len) - all_brick - blank # 最大矩形中所包含的水
                result += water # 总水量
                graph_len = 1 # 重新开始计算矩形的长度
                left_idx = curr_idx # 更新左指针的索引
                left_val = height[left_idx] # 更新左指针的数值
            graph_len += 1
        # 验证是否全部完成
        if left_idx < len(height) - 1:
            # 处理右指针没有左指针大但是还是会储存雨水的情况
            # 反转height中，右指针比左指针小的那一部分
            new_height = list(reversed(height[left_idx:]))
            water = self.trap(new_height)
            result += water
        return result

# Solution().trap([4,2,0,3,2,5])
Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])