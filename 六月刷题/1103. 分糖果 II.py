from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # 初始化结果数组
        sun = [0] * num_people
        # 当前糖果分发数量
        amount = 0
        while True:
            """
            后移
            模永远小于模数
            一旦amount碰到num_people的倍数便会从零开始，amount % num_people = idx（idx < num_people）
            让 amount += 1，既符合了分糖的逐渐累加 1 的要求，又满足了“不断后移人，当到达队伍终点后再次从队伍起点开始”的要求
            """
            idx = amount % num_people
            amount += 1
            sun[idx] += amount

            # 总糖数量去除当前分发出去的糖的数量
            candies -= amount
            # 如果剩下的糖不够下次分发的了则提取更新下一个孩子的糖数并中断循环
            if candies <= amount + 1:
                sun[amount % num_people] += candies
                break
        return sun

candies = 10
num_people = 3
Solution().distributeCandies(candies, num_people)