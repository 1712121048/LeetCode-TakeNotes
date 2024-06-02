from collections import Counter
from typing import List
import numpy as np


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 将多维数组转换为一维数组
        array = [c for r in grid for c in r]
        # 重复数字A
        val_A = Counter(array).most_common()[0][0]
        # 全部数值集合，用于寻找到未在grid出现的数值
        num_dict = [n for n in range(1, len(grid) ** 2 + 1)]
        # 删除数字A
        array.remove(val_A)
        array.remove(val_A)
        num_dict.remove(val_A)
        # 集合差集。找出缺少数字B
        val_B = (set(num_dict) - set(array)).pop()
        sun = [val_A, val_B]
        return sun

grid = [[9,1,7],[8,3,2],[3,4,6]]
Solution().findMissingAndRepeatedValues(grid)