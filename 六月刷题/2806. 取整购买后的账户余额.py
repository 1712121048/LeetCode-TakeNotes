class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # 在 py 中可以使用 round 函数将数字四舍五入到最近的十位数， round() 函数接受两个参数：要四舍五入的数字和要四舍五入到的小数位数。通过将第二个参数设置为负数，可以指定将数字四舍五入到特定的十位数、百位数等
        if purchaseAmount % 5 == 0:
            # 5的话特殊处理一下
            purchaseAmount += 1
        ten_fold = round(purchaseAmount, -1)
        sun = 100 - ten_fold
        return sun

purchaseAmount = 25
Solution().accountBalanceAfterPurchase(purchaseAmount)