from math import inf
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 为了免于四连通处理边距，为grid加入一层空的外墙
        grid = [[0] + n + [0] for n in grid]
        top_below = [0] * len(grid[0])
        grid.insert(0, top_below)
        grid.append(top_below)

        # 四连通
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        # 被感染橙子数组、新鲜橙子数组
        spreads, oranges = ([(x, y, 0) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 2],
                            [(x, y, 0) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 1])
        # 正在执行第几次扩散
        infect = 0 if len(spreads) > 0 else -inf
        # 新鲜橘子被感染的数量
        fresh_num = 0

        # 处理极端情况
        # 如果不存在病原体但是存在新鲜橘子就返回-1
        if len(spreads) == 0 and len(oranges) > 1:
            return -1
        # 如果不存在新鲜橘子就返回零
        elif len(oranges) == 0:
            return 0

        while len(spreads) > 0:
            curr = spreads.pop(0)
            infect = curr[2]
            for i in range(4):
                x, y = curr[0] + dx[i], curr[1] + dy[i]
                if grid[x][y] == 1:
                    # 更新grid里的感染状态
                    grid[x][y] = 2
                    # 被传染上的橘子
                    orange = (x, y, infect + 1)
                    # 将被传染上的橘子加入扩散列表中去。
                    spreads.append(orange)
                    # 记录感染橘子的个数
                    fresh_num += 1

        # 存在断桥的，无法感染全部的新鲜橘子。
        if fresh_num < len(oranges):
            return -1
        return infect

grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2],[0],[1]]
grid = [[0]]
Solution().orangesRotting(grid)