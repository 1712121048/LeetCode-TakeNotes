import math
class Solution:
    def maximumLength(self, s: str) -> int:
        # 分组，先把每组字符出现的连续字符的长度拿出来
        s+= "0"
        record = {}
        l = 0
        for i, n in enumerate(s):
            if s[l] != s[i]:
                if s[l] in record:
                    record[s[l]].append(i - l)
                else:
                    record[s[l]] = [i - l]

                l = i
        sun = -1
        """
        长度为 n 的特殊子字符依次可以得到 n - i 长的字符

        想必通过上述你也能看的出来 特殊字符串中出现三次的最长的字符串 是从特殊字符串开头到 n-2 为止的字符串
        s = "qweaaaaaaaarty"
        
        left = 3
        a			1
        aa			1
        aaa			1
        aaaa		1
        aaaaa		1
        aaaaaa		1
        aaaaaaa		1
        aaaaaaaa	1
        
        left = 4
        a			2	
        aa			2
        aaa			2
        aaaa		2
        aaaaa		2
        aaaaaa		2
        aaaaaaa		2
        aaaaaaaa	1
        
        left = 5
        a			3
        aa			3
        aaa			3
        aaaa		3
        aaaaa		3
        aaaaaa		3
        aaaaaaa		2
        aaaaaaaa	1		
        
        left = 6
        a			4
        aa			4
        aaa			4
        aaaa		4
        aaaaa		4
        aaaaaa		3
        aaaaaaa		2
        aaaaaaaa	1
        """
        # 循环所有所有字符分组
        for n in record:
            """
            1、从最长的特殊子串（a[0]）中取三个长度均为 a[0]−2 的特殊子串。例如示例 1 的 aaaa 可以取三个 aa。
            2、从最长和次长的特殊子串（a[0],a[1]）中取三个长度一样的特殊子串：
                2.1、如果 a[0]=a[1]，那么可以取三个长度均为 a[0]−1 的特殊子串。
                2.2、如果 a[0]>a[1]，那么可以取三个长度均为 a[1] 的特殊子串：从最长中取两个，从次长中取一个。
            3、从最长、次长、第三长的的特殊子串（a[0],a[1],a[2]）中各取一个长为 a[2] 的特殊子串。
            """
            # 只要最大的3个
            ary = sorted(record[n],reverse=True)[:3]
            # 如果总数量不到3个则补上-1
            ary += [-1] * (3 - len(ary))
            max_val = ary.pop(0)
            second_val = ary.pop(0)
            third_val = ary.pop(0)

            # 省去if了，直接写算式
            # 为了可读性 *3、/3
            # 因为要获取的是单个的长度，所以除3
            val1 = ((max_val - 2) * 3) / 3
            val2 = ((3 * (max_val - 1)) * (max_val == second_val) + (second_val * 3) * (max_val > second_val)) / 3
            val3 = (third_val * 3) / 3

            sun = max(sun, val1, val2, val3)
        sun = -1 if sun == 0 else int(sun)
        return sun

    def maximumLength2(self, s: str) -> int:
        # 记录每种字符串出现次数的情况
        record = {}
        #  bbabbbbbo索引从3开始特殊字符串b不能跟索引从0开始的特殊字符串b搞混了
        # 避免与跟s[left]字符相同，但是中间被其他字符断开，两种字符相同但是不属于特殊字符子串的高混乱
        distant_relative = {}
        res = (3, 0)
        # 是否剪枝
        is_pruning = False
        # left的前一个字符串（剪枝验证使用）
        l_pre_str = s[0]
        # 不确定右侧指针的通用大体逻辑
        left, right = 0, 0
        while left < len(s):
            longest = (3, 0)
            is_pruning = False
            while right < len(s):
                # baaxa aaaa
                curr = s[right]
                # left和right的区间是特殊子字符串
                if curr == s[left]:
                    key = s[left: right + 1]
                    num = record.get(key, 0) + 1
                    record[key] = num
                    distant_relative[key] = distant_relative.get(key, 0) + 1
                    right += 1
                    # 如果大于等于3则设置为无限大，否则还是原来的值，因为根本条件是大于3，元组的第二个值则是长度。对比的话使用元组的特性
                    """
                    True：1
                    False：0
                    算式：（num * （num >= 3））-（num * （num < 3））* inf ==（num * 条件A）-（num * 条件B）* inf 
                    如果 num >= 3 则为 条件A 成立为True，条件B则不成立为False
                        当前的结果一定为正数
                        （num * 1） - （num * 0） = num - 0
                    如果 num < 3 则为 条件B 成立为True，条件A则不成立为False
                        当前结果一定为负数
                        （num * 0） - （num * 1） = 0 - num
                    得出了正负数，就可以控制最大最小极数（inf，-inf）
                    
                    为什么使用inf？
                        因为只要满足【出现的次数 > 3】这个硬性条件即可，不必纠结于次数的多少，只要 >=3 就行，所以让全部 >=3 的字符的出现次数全部等于 inf，这样方便使用元组的特性进行对比，然后找长度最长的这个次要条件。
                    元组对比特性：使用元组进行对比ASCII，元组对比的特性：元组之间的比较是逐个元素进行比较的，从左到右按顺序比较元组中对应位置上的元素。
                    """
                    val = (((num * (num >= 3)) - (num * (num < 3))) * math.inf, len(key))
                    longest = max(longest, val)
                    # 剪枝
                    """
                    只有当当前left处于特殊子字符串内部的时候才允许剪枝。
                    前面的当前类型的字符出现次数 >= 3，长度也是所有出现次数大于3的字符里面最长的（longest）而且大于当前字符长度，可进行剪枝
                    避免那种【baax a aaaa】，当left = 4的时候，因为前面出现过a，导致一进来就满足a的次数>=3，就进行剪枝。
                    
                    长度为 n 的特殊子字符依次可以得到 n - i 长的字符
                    
                    s = "qweaaaaaaaarty"
                    
                    left = 3
                    a			1
                    aa			1
                    aaa			1
                    aaaa		1
                    aaaaa		1
                    aaaaaa		1
                    aaaaaaa		1
                    aaaaaaaa	1
                    
                    left = 4
                    a			2	
                    aa			2
                    aaa			2
                    aaaa		2
                    aaaaa		2
                    aaaaaa		2
                    aaaaaaa		2
                    aaaaaaaa	1
                    
                    left = 5
                    a			3
                    aa			3
                    aaa			3
                    aaaa		3
                    aaaaa		3
                    aaaaaa		3	（被选中）
                    aaaaaaa		2
                    aaaaaaaa	1					
                    
                    left = 6
                    a			4（前面的【aaaaaa】出现次数 >= 3，长度也是所有出现次数大于3的字符里面最长的（longest）而且大于当前字符长度，可进行剪枝），选中了前面的【aaaaaa】，而且是有规律的：left + len(longest)刚好走出去当前特殊字符子串。比如：left（6） + longest.length （6） = 12。s[12 - 1] 刚好是走出 a 的特殊字符子串的之后的第一个。
                    aa			3（剪掉）
                    aaa			3（剪掉）
                    aaaa		3（剪掉）
                    aaaaa		3（剪掉）
                    aaaaaa		3（剪掉）
                    aaaaaaa		2（略过）
                    aaaaaaaa	1（略过）
                    
                    bbabbbbbo索引从3开始特殊字符串b不能跟索引从0开始的特殊字符串b搞混了,只有满足distant_relative记录的前面的字符出现次数 >= 3，长度也是所有出现次数大于3的字符里面最长的（longest）而且大于当前字符长度，才可进行剪枝
                    想必通过上述你也能看的出来 特殊字符串中出现三次的最长的字符串 是从特殊字符串开头到 n-2 为止的字符串
                    """
                    if longest > val and longest[1] > val[1] and l_pre_str == s[left]:
                        key = "".join([curr]*longest[1])
                        if distant_relative.get(key, 0) >= 3:
                            is_pruning = True
                            break
                else:
                    if left < len(s) and s[left] != s[left + 1]:
                        distant_relative = {}
                    # 恢复现场。初始的时候就是：left=right。
                    l_pre_str = s[left]
                    left += 1
                    right = left

            # 更新结果
            res = max(res, longest)
            # 剪枝
            if is_pruning:
                left += max(longest[1], 1) - 1
            else :
                left += 1
            right = left

        sun = -1 if res[1] == 0 else res[1]
        return sun

s = "abcdeefghe"
s = "qweaaaaarty"
s = "qweaaaaaaaarty"
s = "aaaaa"
s = "bbcbabbabbb"
s = "bab"
Solution().maximumLength(s)


