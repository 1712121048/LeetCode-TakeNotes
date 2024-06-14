import itertools
from typing import List

class Solution:
    """
    行纵不能相交
    X 不存在 X 的 x轴和y轴同时挨着另一个 X 的情况
    """
    def countBattleships(self, board: List[List[str]]) -> int:
        sun = 0
        # 先取出全部 战舰 的坐标
        coordinate_X = [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == 'X']
        # 验证极端情况
        if len(coordinate_X) == 0:
            return sun
        else:
            # 获取临近战舰
            def get_adjoin(curr, direction):
                # 四连通
                dx = [-1, 1, 0, 0]
                dy = [0, 0, -1, 1]
                i = direction - 1 + (direction - 1) if direction > 0 else direction * -1 + (direction * -1 - 1)
                adjoin = (curr[0] + dx[i], curr[1] + dy[i])
                return adjoin

            # 记录起点和当前走到哪里了
            record = None
            # 记录方向：1-上，-1-下，2-左，-2-右
            direction = 0

            # 要弹出的索引
            pop_idx = 0
            while len(coordinate_X) > 0:
                # 当前战舰
                curr = coordinate_X.pop(pop_idx)
                if direction == 0:
                    # 确定方向
                    for n in [1, -1, 2, -2]:
                        # 临近节点
                        adjoin = get_adjoin(curr, n)
                        if adjoin in coordinate_X:
                            # 记录方向
                            direction = n
                            # 记录本舰队从以curr开始走的
                            record = (curr, adjoin)
                            # 下一次要弹出的战舰
                            pop_idx = coordinate_X.index(adjoin)
                            break
                    sun += 1
                else:
                    # 获取临近节点
                    adjoin = get_adjoin(curr, direction)
                    # 下一次要弹出的战舰
                    if adjoin in coordinate_X:
                        record = (record[0], adjoin)
                        pop_idx = coordinate_X.index(adjoin)
                    else:
                        # 折返回起点，逆向搜索
                        direction = direction * -1
                        # 获取起点逆向的临近节点
                        adjoin = get_adjoin(record[0], direction)

                        if adjoin in coordinate_X:
                            # 起点逆向存在临近节点
                            pop_idx = coordinate_X.index(adjoin)
                        else:
                            # 逆向也不存在临近节点，重新从 coordinate_X 的第一艘战舰寻找战队
                            pop_idx = 0
                            direction = 0
                            record = None
            return sun

board = [["X",".",".","X"],[".",".",".","X"],["X","X",".","."],[".",".","X","."],["X",".","X","."]]
board = [["X",".","X","."],["X",".",".","."],["X",".","X","X"],["X",".",".","."],["X",".","X","X"]]
Solution().countBattleships(board)