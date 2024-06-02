from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        result = [0] * width
        for idx, row in enumerate(grid):
            for i, col in enumerate(row):
                col_len = len(str(col))
                result[i] = max(result[i],col_len)
        return result

Solution().findColumnWidth([[1],[22],[333]])