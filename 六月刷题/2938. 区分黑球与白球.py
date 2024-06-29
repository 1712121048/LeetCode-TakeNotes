from collections import Counter
class Solution:
    # 这道题是移动不是交换
    def minimumSteps(self, s: str) -> int:
        # 结果
        sun = 0
        # 当前 0 之前出现的 1 的个数
        one_amount = 0
        for n in s:
            if n == "1":
                one_amount += 1
            else:
                sun += one_amount
        return sun

    # 我错误的理解成为交换了
    def minimumSteps2(self, s: str) -> int:
        sun = 0
        s_ary = list(s)
        # left 永远指向索引最大的白球
        # right 永远指向索引最小的黑球
        left, right = s.rindex("0"), s.index("1")
        while left > right:
            temp = s_ary[left]
            s_ary[left] = s_ary[right]
            s_ary[right] = temp
            left, right = str.join("",s_ary).rindex("0"), str.join("",s_ary).index("1")
            sun += 1
        return sun

s = "101"
Solution().minimumSteps(s)