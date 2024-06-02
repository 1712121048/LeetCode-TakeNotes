from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        注意条件：1 <= rolls[i], mean <= 6

        rolls = [1, 2, 3, 5, 6, 3]
        mean = 3
        n = 4
        方程：(sum(1, 2, 3, 5, 6, 3) + x) / (n + len(rolls)) = mean。求x
        (20 + x) / 10 = 3
        (20 + x) = 3 * 10
        20 + x = 30
        x = 30 - 20
        x = 10
        如果 x 小于等于 n*6，则说明 x 是可以被分成 n 个小于等于 6 的数值集合的，也就符合条件（1 <= rolls[i], mean <= 6）了，因为1 <= rolls[i]所以x也不能是负数。
        """
        sun = []
        addend = sum(rolls)
        all_num = n + len(rolls)
        right_item = mean * all_num
        x = right_item - addend

        # 找到 n 个整数，使得它们的和为 𝑟，不得出现0，否则返回空数组
        def distribute_ints(n, r):
            base = r // n
            remainder = r % n
            result = [base] * n
            for i in range(remainder):
                result[i] += 1
            if 0 in set(result):
                return []
            return result
        if x > 0 and x <= n * 6:
            sun = distribute_ints(n, x)
        return sun

rolls = [1,2,3,5,6,3]
mean = 6
n = 4

rolls = [1,5,6]
mean = 3
n = 4

# rolls = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3]
# mean = 2
# n = 53
Solution().missingRolls(rolls, mean, n)