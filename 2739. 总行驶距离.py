# 卡车有两个油箱。给你两个整数，mainTank
# 表示主油箱中的燃料（以升为单位），additionalTank
# 表示副油箱中的燃料（以升为单位）。
# 该卡车每耗费1升燃料都可以行驶10km。每当主油箱使用了5升燃料时，如果副油箱至少有1升燃料，则会将1升燃料从副油箱转移到主油箱。返回卡车可以行驶的最大距离。
# 注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗5升燃料时突然且立即发生。

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_distance = 0
        while mainTank > 0:
            if mainTank >= 5:
                if additionalTank > 0:
                    # 副油箱额外补一，所以减四
                    mainTank -= 4
                    additionalTank -= 1
                else:
                    mainTank -= 5
                total_distance += 50
            else:
                total_distance += mainTank * 10
                mainTank = 0
        return total_distance