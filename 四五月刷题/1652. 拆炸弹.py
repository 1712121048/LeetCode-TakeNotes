from typing import List


class Solution:
    # [2,4,9,3]
    def decrypt(self, code: List[int], k: int) -> List[int]:
        tow_code = code * 2 # 让我想起来处理环的方法
        code_len = len(code)
        if k > 0:
            for i in range(code_len):
                code[i] = sum(tow_code[i + 1:(i + k) + 1])
        elif k < 0:
            for i in range(code_len, len(tow_code)):
                code[i - code_len] = sum(tow_code[i + k: i])
        elif k == 0:
            return [0] * code_len


code = [2,4,9,3]
k = -2
Solution().decrypt(code, k)