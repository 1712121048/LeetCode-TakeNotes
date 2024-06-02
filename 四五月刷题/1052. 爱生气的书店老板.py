from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 窗口内原本满意的客人
        window_val_zero = 0
        # 窗口内原本不满意的客人
        window_val_one = 0
        # 使用窗口的右指针作为key，计算出窗口内满意和不满意的顾客分别有多少，并将其作为字典的value
        window_dict = {}
        # 所有满意的顾客
        total_val = 0
        for i, n in enumerate(grumpy):
            # 窗口滑动，右进左出
            if n == 0:
                # 窗口的zero部分进行右进
                window_val_zero += customers[i]
                total_val += customers[i]
            else:
                # 窗口的one部分进行右进
                window_val_one += customers[i]

            # 已经形成窗口
            if i + 1 >= minutes:
                # 计算要被左出的左指针
                left = i - minutes
                if left >= 0:
                    # 左出
                    if grumpy[left] == 0:
                        # 如果要被出去的左指针原本是窗口的zero部分的，则对窗口的zero部分进行左出
                        window_val_zero -= customers[left]
                    else:
                        # 如果要被出去的左指针原本是窗口的one部分的，则对窗口的one部分进行左出
                        window_val_one -= customers[left]
                # 将当前窗口信息加入字典当中
                window_dict[i] = (window_val_zero, window_val_one)
        result = 0
        for i, n in enumerate(customers):
            # 计算右指针
            right = i + minutes - 1
            # 右指针超出列表则表示查询完成，终止循环
            if right >= len(customers):
                break
            # 通过操作可得数值（窗口内的值）
            interior_val = window_dict[right][0] + window_dict[right][1]
            # 本身应得的（窗口外的grumpy[i]为0的customers[i]值）
            outside_val = total_val - window_dict[right][0]
            # 本身应得+努力所得=最终所得
            result = max((interior_val + outside_val), result)
        return result

    # 解法2（在超大数据面前超时）
    def maxSatisfied2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result = 0
        for i, n in enumerate(customers):
            left = i
            right = i + minutes - 1
            if right >= len(customers):
                break
            interior_val = sum(customers[left : right + 1])
            outside_val = self.get_window_out_max_val(customers,grumpy,left,right)
            result = max((interior_val + outside_val), result)
        return result
    # 窗口以外所能获取到的最大值
    def get_window_out_max_val(self, customers: List[int], grumpy: List[int], left:int, right:int):
        new_grumpy = grumpy[:]
        new_grumpy[left:right + 1] = [1] * (right + 1 - left)
        indexs = [i for i, x in enumerate(new_grumpy) if x == 0]
        value = sum(map(lambda a: customers[a],indexs))
        return value

zero = 1+3 -1 +5
one = 2+4 -2
customers = [1,2,3,4,5,6,7,8]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
Solution().maxSatisfied2(customers,grumpy,minutes)