ary = [0, 0, 0]

class Solution:
    # 必须将所有糖果分发完
    def distributeCandies(self, n: int, limit: int) -> int:
        return self.distributeCandies2(n, limit,0,0,0, [])

    """
    :param n: 糖果总数
    :param limit: 每个孩童最多所得
    :param allocated: 已经分配出去的糖果数量
    :param level: 当前是第几个小朋友
    :param sun: 总共分配方法
    :return:
    """
    def distributeCandies2(self, n: int, limit: int, allocated: int, level: int, sun: int, res = []) -> int:
        global ary
        amount = 0
        while amount <= limit and allocated + amount < n:
            # 使用的是上一次的amount
            if level < 2 and allocated + amount < n:
                ary[level] = amount
                sun, res = self.distributeCandies2(n, limit, allocated + amount, level + 1, sun, res)
                ary[level] = 0
            # 下一次使用
            amount += 1

        if allocated + amount == n and amount <= limit:
            ary[level] = amount
            res.append(list(ary))
            ary[level] = 0
            sun += 1
        return sun, res
n = 3
limit = 2
Solution().distributeCandies(n, limit)