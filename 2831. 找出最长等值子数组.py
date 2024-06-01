from collections import Counter
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        sun = 0
        # 将字符和字符的索引存入（key：字符，value：相同字符的所有索引）
        """
        [1,2,3,1,2,5,6,6,1,6]：
        {
            1: [0, 3, 8], 
            2: [1, 4], 
            3: [2], 
            5: [5], 
            6: [6, 7, 9]
        }
        不过因为我们是找最长等值子数组，具体是最长等值子数组属于哪一个字符我们不在乎
        （最长等值子数组属于谁我不在乎）
        """
        num_dict = {}
        for i, n in enumerate(nums):
            if n not in num_dict:
                num_dict[n] = [i]
            else:
                num_dict[n].append(i)
        nums_idxs = list(num_dict.values())
        # 按照二维数组中一维数组的长度倒序排序
        nums_idxs = sorted(nums_idxs, key=len, reverse=True)
        # 循环所有种类的字符
        while len(nums_idxs) > 0:
            idxs = nums_idxs.pop(0)
            # 如果当前字符的累计长度都不大于sun，则说明当前的字符的等值子数组的长度是不可能大于sun的，因为已经排序了，当前的等值子数组的长度都不会大于sun了，后面的长度也不可能大于，所以终止循环，sun就是最大长度
            if len(idxs) <= sun:
                break

            # 当前字符在满足k的情况下可以出现的最大次数
            single_max = 0
            # 双指针
            left, right = 0, 0

            # 当前字符在left和right之间出现的次数（不含left）
            curr_num = -1
            """
            [1,2,1]
                1：[0,2]
            0

            [1,2,1]
                1：[0,2]
            1
            """
            flag = False
            # 当前字符最多能组成多大的等值子数组。
            # [1,9,8,7, 1, 11, 1, 10, 1 ,6, 1,1, 3, 1]
            while right < len(idxs):
                # idxs[r]-idxs[left]-1-curr_num：在原始列表中idxs[r]到idxs[left]之间有几个抛去当前字符的正整数（有几个阻挡当前字符连续的碍脚石）
                amount = idxs[right] - idxs[left] - 1 - curr_num
                if amount <= k:
                    # k仍然可以满足上次right+1之后的去除left——right之间碍脚石的条件，所以接着为right扩展右指针
                    curr_num += 1
                    right += 1
                    flag = False
                else:
                    # k已经被用光了，从left——right是k所能完成curr_num的最大极限了。
                    """
                     k已经被用光了，右指针停下左指针前进。
                     接下来进行窗口滑动尝试新的区间，left前进，right保持在上次停下的位置，因为左指针前进一位所以left——right之间的当前字符个数得减去一位（curr_num -= 1）。
                    """
                    left += 1
                    right = max(left, right)
                    # curr_num + 1表示：把left的那个字符的个数也给加上
                    single_max = max(single_max, curr_num + 1)
                    flag = True
                    # 由余左节点进行了前进，所以从出现次数（curr_num）当中减去一位
                    curr_num -= 1

            # 解决right+1数位后移之后right不小于len(idxs)导致循环断开，single_max没有即时更新到的情况
            if not flag:
                # curr_num + 1表示：把left的那个字符的个数也给加上
                single_max = max(single_max, curr_num + 1)
            # 如果当前字符的等值子数组的长度大于已知的等值子数组的长度，则更新sun
            sun = max(sun, single_max)
        return max(sun, 1)

nums = [1,2,3,1,5,6,1,7, 1 ,9,8,7, 1, 11, 1 ,12,1,13,1,1,15,1]
k = 4
# nums = [1,9,8,7,1,2,3,1,5,6,1,7,1,9,1]
# k = 4
# nums = [1,2,1]
# k = 1
nums = [1,2,3,1,2,5,6,6,1,6]
k = 0
Solution().longestEqualSubarray(nums, k)