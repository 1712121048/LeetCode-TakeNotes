class Solution:
    def numberToWords(self, num: int) -> str:
        # single digit
        base_singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        # tens digit
        base_tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        # whole
        base_wholes = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        # big
        base_bigs = ["Hundred", "Thousand", "Million", "Billion"]

        str_num = str(num)
        def dfs(val, digit):
            nonlocal base_singles, base_tens, base_wholes, base_bigs
            # 先算数，最后加单位
            res = ""
            curr = int(val) if len(val) < 3 else int(val[len(val) - 3:])
            if curr < 10:
                # 分组之后，当前为个位
                res = base_singles[curr]
            elif curr < 100:
                # 分组之后，当前为十位
                res = tens_digit_handle(curr)
            else:
                # 分组之后，当前组是百位
                hundred = int(curr / 100)
                surplus = curr - hundred * 100
                ten = ""
                if surplus < 10:
                    ten = base_singles[surplus]
                else:
                    ten = tens_digit_handle(surplus)
                res = base_singles[hundred] + " Hundred And " + ten
            # 最后是单位
            if res != "":
                res += "" if digit == 0 else " " + base_bigs[digit]
            # 下一次递归
            next = "" if len(val) - 3 < 1 else val[:len(val) - 3]
            if len(next) > 0:
                res = dfs(next, digit + 1) + (" " + res if res != "" else "")
            return res
        def tens_digit_handle(curr):
            # 处理十位数
            nonlocal base_singles, base_tens, base_wholes
            sun = ""
            if curr == 0:
                pass
            elif curr < 20:
                # 特殊十位
                ten = curr - 10
                sun = base_tens[ten]
            else:
                # 组合十位
                ten = int(curr / 10)
                single = curr - ten * 10
                sun = base_wholes[ten] + " - " + base_singles[single]
            return sun

        sun = ""
        if num == 0:
            # 零特殊处理
            sun = "Zero"
        elif len(str_num) == 1:
            # 个位
            sun = base_singles[num]
        elif len(str_num) == 2:
            # 十位
            sun = tens_digit_handle(num)
        else:
            # 大位数，进行递归
            sun = dfs(str_num, 0)

        # 多个 replace 方法链式调用时，可能会遇到意外的结果
        # sun = (sun.replace(" And", "").replace(" -", "").replace("  ", " "))
        # 移除 And 和 -
        sun = str.join("",str.join("", sun.split(' And')).split(" -"))
        # 移除前后空格
        sun = sun.strip()
        # 移除连续空格
        sun = str.join(" ", list(filter(lambda a: a != "", sun.split(' '))))
        return sun

num = 2147483647
num = 171212
num = 1712
# num = 171
# num = 107
# num = 99
# num = 90
# num = 19
num = 1000000001
num = 50868
Solution().numberToWords(num)