class formula_tree:
    def __init__(self, formula: str, is_add=True, val=0):
        # 公式
        self.formula = formula
        # 是否被加
        self.is_add = is_add
        # 子节点
        self.childs = []
        # 序号
        self.sequence = 0
        # 公式值
        self.val = val

class Solution:
    def calculate(self, s: str) -> int:
        s.replace(' ', '')
        tree = self.build_formula_tree(s, formula_tree("", True, 0))
        tree.val = sum(map(lambda child: child.val if child.is_add else -child.val, tree.childs))
        return tree.val

    # 将公式转化成formula_tree类
    def build_formula_tree(self, s: str, f_tree: formula_tree):
        # 记录括号
        record_brackets = 0
        # 记录上一次切割位置
        last_position = 0
        # 清除公式中的空格
        s = s.replace(" ","")
        # 清除当前公式的总括号
        if self.validator_all_brackets(s):
            s = s[1:-1]
        # 因为每次截取都要带着前面的运算符，开头可能不存在运算符，所以加上个默认的
        if not s.startswith("+") and not s.startswith("-"):
            s = "+" + s
        # 因为是获取“上次切割处之后和本次扫描的运算符之前的那段公式”，如果不在末尾加上额外的运算字符那么上次切割处后面的那段公式就不会被收录
        s += "+"
        for i, n in enumerate(s):
            validator = self.validator_int(n)
            if n == "(":
                record_brackets += 1
            elif n == ")":
                record_brackets -= 1
            # 当前扫描处索引不是零并且不属于括号里的并且是（+/-）的，在当前扫描处前面和上次断开处截取
            if not validator and i > 0 and record_brackets == 0 and not n == "(" and not n == ")":
                formula = s[last_position:i]
                is_add = not formula.startswith("-")
                formula = formula[1:]
                is_val = self.validator_int(formula)
                tree = formula_tree(formula, is_add, 0)
                if is_val:
                    tree.val = int(formula)
                else:
                    tree = self.build_formula_tree(formula, tree)
                    tree.val = sum(map(lambda child: child.val if child.is_add else -child.val, tree.childs))
                tree.sequence = len(f_tree.childs) + 1
                f_tree.childs.append(tree)
                last_position = i
        return f_tree

    # 验证能否转化为int类型
    def validator_int(self, num_str: str):
        try:
            val = int(num_str)
            return True
        except:
            return False

    # 验证公式是否存在总括号
    def validator_all_brackets(self, formula: str):
        validator = False
        l_brackets = []
        r_brackets = []
        if formula.startswith("(") and formula.endswith(")"):
            formula = formula[1:-1] # 尝试去掉最外层的一层括号，看看剩下的是否合法
            for i,n in enumerate(formula):
                if n == "(":
                    l_brackets.append("(")
                elif n == ")":
                    r_brackets.append(")")
                if len(r_brackets) > len(l_brackets):
                    break
            if len(l_brackets) == len(r_brackets):
                validator = True
        return validator

    # 解题方法二（栈解决）
    def calculate2(self, s: str) -> int:
        # "178-2-(1-(3+5)+2)"、"178-2+(1-(3+5)+2)"
        res,sign,num=0,1,0 # 结果、符号、当前数字
        record = [] # 记录每一层括号之前的那个运算符
        s = s.replace(" ","") # 清除表达式空格
        # 这tm居然有“123”这种用例，改一下表达式
        s+="+0"
        i = 0
        while i < len(s):
            if s[i] >= "0" and s[i] <= "9":
                # 数字
                for idx in range(i,len(s)):
                    # 数字后面不可能是"("，只能是加减和“)”，所以不用验证s[idx]是否为“(”
                    if s[idx] == '-' or s[idx] == "+" or s[idx] == ")":
                        i=idx
                        break
                    num = num*10+int(s[idx]) # 计算技巧
                res += num*sign
                num = 0

            if s[i] == "+":
                # 因为如果括号之前是减号，那么括号内的计算符号就取相反
                # 假设如果记录中第一个括号外面是一个减号，当前扫描到括号内部中这个加号了（既然存在前提：括号外的符号是减号的话括号内的符号取反），那么本次加号应该去相反的符号，也就是减号，换句话说也就是得把sign换成负一，record最后一个符号记录了本括号外的符号，也就是记录了-1，那么 -1*1=-1，这样就取得了相反的符号
                sign = record[-1] * 1 if len(record) > 0 else 1
            elif s[i] == "-":
                # 套用上述描述，如果record所记录的本层括号是负数则：-1*-1=1，如果记录的本层括号是整数也就是记录的1，1乘任何数都不变
                sign = record[-1] * -1 if len(record) > 0 else -1
            elif s[i] == "(":
                record.append(sign)
            elif s[i] == ")":
                record.pop()
            i += 1
        return res

# Solution().calculate("(-0)-1-(1+(4+5+2)-3)")
# Solution().calculate("(-2)-1-(1+(4+5+2)-3)+1")
# Solution().calculate("-1-(1+(4+5+2)-3)")
Solution().calculate2("123")