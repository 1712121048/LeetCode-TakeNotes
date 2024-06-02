from typing import List


class Solution:
    """
    输出的答案要和预期结果一模一样，连下标位置都要一模一样，不然判定解答错误。
    """
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # 全胜
        AK = set()
        # 输一次
        AC = set()
        # 输掉的次数>1（加入黑名单）
        WA = set()
        while len(matches):
            # 本场赛事输赢双方
            win, lose = matches.pop(0)
            # 当前win在此之前输掉了多长比赛（不配进入AK）
            if win in WA:
                pass
            # 当前win在此之前输掉了一场比赛（不配进入AK）
            elif win in AC:
                pass
            # win是第一次现身便胜利，加入AK
            elif win not in AK:
                AK.add(win)

            # lose在此之前已经输了多次了
            if lose in WA:
                pass
            # lose在此之前已经输过一次了，这次又输了，取消AC资格，加入黑名单
            elif lose in AC:
                AC.discard(lose)
                WA.add(lose)
            # lose之前从未输过，这是第一次输掉比赛，剥夺AK资格，加入AC行列
            elif lose in AK:
                AK.discard(lose)
                AC.add(lose)
            # lose头一次现身就输掉比赛，直接加入AC行列
            elif lose not in AC:
                AC.add(lose)

        AK = sorted(list(AK))
        AC = sorted(list(AC))
        sun = [AK, AC]
        return sun

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
matches = [[4,5],[2,3],[5,4],[6,4]]
matches = [[1,2],[16,1]]
Solution().findWinners(matches)