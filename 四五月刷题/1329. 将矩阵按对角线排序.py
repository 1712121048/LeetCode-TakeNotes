from typing import List
from math import inf

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        # 列
        for c in range(col_len):
            # 行
            for r in range(row_len):

                # region 写法一
                # # 对角线
                # last_row = r  # 上一个对角线的行
                # last_col = c  # 上一个对角线的列
                # row = r
                # col = c
                # while not (col >= col_len or row >= row_len):
                #     if mat[last_row][last_col] > mat[row][col]:
                #         last_val = mat[last_row][last_col]
                #         mat[last_row][last_col] = mat[row][col]
                #         mat[row][col] = last_val
                #     last_row = row
                #     last_col = col
                #     row += 1
                #     col += 1
                # endregion

                # 对角序列
                diagonal = []
                # 对角线
                row = r
                col = c
                while not (col >= col_len or row >= row_len):
                    diagonal.append(mat[row][col])
                    row += 1
                    col += 1
                # 重新设置对角线
                diagonal.sort()
                row = r
                col = c
                while not (col >= col_len or row >= row_len):
                    mat[row][col] = diagonal.pop(0)
                    row += 1
                    col += 1
        return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Solution().diagonalSort(mat)