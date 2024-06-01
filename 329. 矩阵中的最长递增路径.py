from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 0
        record = [[None for _ in range(len(matrix[-1]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[-1])):
                if record[r][c] is None:
                    val, record = self.dfs_matrix(matrix, record, r, c)
                    record[r][c] = val
                    result = max(result, val)
        return result

    # 对指定的节点进行深度搜索
    def dfs_matrix(self, matrix, record, *node):
        result = 0
        cur_r, cur_c = node
        boundary = (0,len(matrix)-1,0,len(matrix[-1])-1)
        around = self.get_four_unicom(boundary,cur_r, cur_c)
        for r, c in around:
            if matrix[r][c] > matrix[cur_r][cur_c]:
                if record[r][c] is None:
                    val, record = self.dfs_matrix(matrix, record, r, c)
                    record[r][c] = val
                    result = max(result, val)
                else:
                    result = max(result, record[r][c])
        return result+1, record


    # 四连通，获取节点的上下左右
    def get_four_unicom(self, boundary, *origin):
        # 提取边界
        min_top, max_below, min_left, max_right = boundary
        r, c = origin
        top = (max(r - 1, min_top), c)
        below = (min(r + 1, max_below), c)
        left = (r, max(c - 1, min_left))
        right = (r, min(c + 1, max_right))
        return top, below, left, right

matrix = [[3,4,5],[3,2,6],[2,2,1]]
#matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,2,3,5,6],[4,3,4,7,7],[5,4,3,6,5]]
Solution().longestIncreasingPath(matrix)
