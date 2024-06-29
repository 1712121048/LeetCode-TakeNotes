import math
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sun = []
        # 拆分字符串
        words = sentence.split(' ')
        for n in words:
            new_str = n
            if new_str.startswith("$"):
                if new_str[1:].isdigit():
                    new_str = "$" + "{:.2f}".format(int(new_str[1:]) - int(new_str[1:]) * discount / 100)
            sun.append(new_str)
        return " ".join(sun)

sentence = "there are $1 $2 and 5$ candies in the shop $12356789012a $ $1235678901 "
discount = 57
Solution().discountPrices(sentence, discount)