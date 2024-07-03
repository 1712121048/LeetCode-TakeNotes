class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sun = -1
        str_x = str(x)
        # 合计数位
        digit = sum(int(char) for char in str_x if char.isdigit())
        if x % digit == 0:
            sun = digit
        return sun

x = 23
Solution().sumOfTheDigitsOfHarshadNumber(x)