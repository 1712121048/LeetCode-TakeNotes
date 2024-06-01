from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        如果两条路径同时出发会有以下几种状态
        路径A：x1，y1
        路径B：x2，y2
        总步数：step_num
        y1的计算方式：step_num - x1
        y2的计算方式：
        """


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
grid = [[1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1]]
Solution().cherryPickup(grid)