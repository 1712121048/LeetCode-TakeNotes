class Solution:
    def maximumLength(self, s: str) -> int:
        # abcdeefghe
        # abcdffeeeefghe
        # abcdffeeee
        # abcdffeeeeqqee
        # aaaaa
        sun = -1
        record = {}
        # 不确定右侧指针的通用大体逻辑
        left, right = 0, 0
        while left < len(s):
            while right < len(s):
                curr = s[right]
                if curr == s[left]:
                    key = s[left: right + 1]
                    record[key] = record.get(key, 0) + 1
                    right += 1
                else:
                    # 恢复现场。初始的时候就是：left=right。
                    # left = right
                    # last_char = s[left]
                    left += 1
                    right = left
            left += 1
            right = left

        while len(record):
            curr = record.popitem()
            if curr[1] >= 3:
                sun = max(sun, len(curr[0]))
        return sun

s = "abcdeefghe"
# s = "aaaaa"
s = "abcdffeeee"
Solution().maximumLength(s)