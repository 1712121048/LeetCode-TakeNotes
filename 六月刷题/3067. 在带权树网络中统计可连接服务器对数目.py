import operator
from collections import Counter
from functools import reduce
from typing import List

# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/solutions/2806953/gai-bian-xian-chang-zhi-hou-yi-ding-yao-lyjas
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        sun = [0] * (len(edges) + 1)
        nodes_info, weights_info = self.get_map_info(edges)
        validator = [[False] * (len(edges) + 1) for _ in range(0, len(edges) + 1)]
        for n in range(0, len(edges) + 1):
            # 是否叶子节点
            if len(nodes_info[n]) < 2:
                continue
            children = self.dfs(n, nodes_info, weights_info, signalSpeed, 0, list(validator), 0)
            # 乘法原理
            num = 0
            left, right = 0, 0
            prefix = 0
            while right < len(children):
                if left == right:
                    num += prefix * children[right]
                    left = 0
                    right += 1
                    prefix = 0
                else:
                    prefix += children[left]
                    left += 1
            sun[n] = num
        return sun

    # 返回以 curr 为根的所有子树上距离满足被signalSpeed整除的节点数集合
    def dfs(self, curr, nodes_info, weights_info, signal_speed, total_weight, validator, level):
        children = []
        for n in nodes_info[curr]:
            # 已经走过的不允许重复走
            if validator[curr][n]:
                continue
            # 标记为已走过（改变现场）
            validator[curr][n] = True
            validator[n][curr] = True

            # curr 至 n 的权值
            weight = weights_info[curr][n]
            # 是否倍数
            flag = (total_weight + weight) % signal_speed == 0
            if len(nodes_info[n]) > 1:
                temp_children = self.dfs(n, nodes_info, weights_info, signal_speed, total_weight + weight,
                                         validator, level + 1)
                if flag:
                    temp_children = [sum(temp_children) + 1]
                children += temp_children
            else:
                if flag:
                    children.append(1)
            # 恢复现场，改变了现场就一定要恢复
            validator[curr][n] = False
            validator[n][curr] = False
        if level == 0:
            return children
        return [sum(children)]

    """
    返回图的信息（所有节点的连接情况）
    1、返回所有节点分别都连接到哪些节点
    2、返回所有两个连接点的权值
    """
    def get_map_info(self, edges: List[List[int]]):
        # key节点分连接value节点
        nodes_info = {}
        # 二维数组，两个连接节点的权值是多少
        weights_info = [[0] * (len(edges) + 1) for _ in range(len(edges) + 1)]
        for n in edges:
            # 权值信息加入 weights_info 中去
            weights_info[n[0]][n[1]] = n[2]
            weights_info[n[1]][n[0]] = n[2]
            # 节点连接信息加入 nodes_info 中去
            if n[0] in nodes_info:
                nodes_info[n[0]].append(n[1])
            else:
                nodes_info[n[0]] = [n[1]]

            if n[1] in nodes_info:
                nodes_info[n[1]].append(n[0])
            else:
                nodes_info[n[1]] = [n[0]]

        return nodes_info, weights_info

#region 记忆化搜索
class Solution3:
    # 记忆化搜索
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        nodes_info, weights_info = self.get_map_info(edges)
        memoryer = [[None] * (len(edges) + 1) for _ in range(0, (len(edges) + 1))]
        sun = [0] * (len(edges) + 1)

        # 深搜，加入记忆体 memoryer 中
        def memory(curr, nodes_info, weights_info, signal_speed, validator):
            # 回的时候入记忆化
            nonlocal memoryer

            # curr 及其子节点的权值信息
            weights = [[] for _ in range(0, max(max(nodes_info[curr]), 1) + 1)]
            # 遍历以当前节点为根的所有子节点
            for n in nodes_info[curr]:
                if validator[curr][n]:
                    continue
                # 改变现场
                validator[curr][n] = True
                validator[n][curr] = True
                # 当前权值
                weight = weights_info[curr][n]
                weights[n].append(weight)
                # 回溯
                children = memory(n, nodes_info, weights_info, signal_speed, validator)
                for nodes_weights in children:
                    for child_weight in nodes_weights:
                        weights[n].append(weight + child_weight)
                # 加入记忆化，叶子结点不加入记忆体
                if memoryer[curr][n] is None:
                    memoryer[curr][n] = list(weights[n])

                # 恢复现场，改变完成现场之后一定要把现场恢复
                validator[curr][n] = False
                validator[n][curr] = False
            return weights

        # 节点连接信息和权值信息
        nodes_info, weights_info = self.get_map_info(edges)

        # 避免重复走来走去
        validator = [[False] * (len(edges) + 1) for _ in range(0, len(edges) + 1)]
        for n in range(0, len(edges) + 1):
            # 是否叶子节点
            if len(nodes_info[n]) < 2:
                continue

            # 记忆化
            memory(n, nodes_info, weights_info, signalSpeed, validator)
            # 记录 n 的每个子节点下能被 signalSpeed 整除的节点数量
            children = []
            for neighbour in nodes_info[n]:
                amount = 0
                for val in memoryer[n][neighbour]:
                    if val % signalSpeed == 0:
                        amount += 1
                if amount > 0:
                    children.append(amount)

            # 乘法原理
            num = 0
            left, right = 0, 0
            prefix = 0
            while right < len(children):
                if left == right:
                    num += prefix * children[right]
                    left = 0
                    right += 1
                    prefix = 0
                else:
                    prefix += children[left]
                    left += 1
            sun[n] = num

        return sun

    """
    返回图的信息（所有节点的连接情况）
    1、返回所有节点分别都连接到哪些节点
    2、返回所有两个连接点的权值
    """
    def get_map_info(self, edges: List[List[int]]):
        # key节点分连接value节点
        nodes_info = {}
        # 二维数组，两个连接节点的权值是多少
        weights_info = [[0] * (len(edges) + 1) for _ in range(len(edges) + 1)]
        for n in edges:
            # 权值信息加入 weights_info 中去
            weights_info[n[0]][n[1]] = n[2]
            weights_info[n[1]][n[0]] = n[2]
            # 节点连接信息加入 nodes_info 中去
            if n[0] in nodes_info:
                nodes_info[n[0]].append(n[1])
            else:
                nodes_info[n[0]] = [n[1]]

            if n[1] in nodes_info:
                nodes_info[n[1]].append(n[0])
            else:
                nodes_info[n[1]] = [n[0]]

        return nodes_info, weights_info

#endregion

#region 实际是图，我却错误理解成“树”了
class Solution2:
    def countPairsOfConnectableServers2(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        sun = [0] * (len(edges) + 1)
        # 节点连接信息和节点连接权值信息
        nodes_info, weights_info = self.get_map_info(edges)

        # 深搜
        for n in range(0, (len(edges) + 1)):
            if len(nodes_info[n]) >= 2:
                # 以 n 为根时的情况
                res = [0] * (len(edges) + 1)
                # 防止重复走
                repeat = [[False] * (len(edges) + 1)] * (len(edges) + 1)
                temp_children_info, children_route = self.dfs(n, signalSpeed, nodes_info, weights_info, repeat, res)
                sun[n] = self.count_pair_permutations(children_route)
        return sun

    # 回溯取得所有节点下面分别有多少个权值为 signalSpeed 的倍数的节点信息
    def dfs(self, curr, signal_speed, nodes_info, weights_info, repeat, res):
        # curr 为叶子节点
        if curr not in nodes_info:
            return []

        # 当前节点及子节点的权值信息
        down_total_weights = []
        # 子节点对应和合格路径情况
        children_route = []
        # 枚举
        for n in nodes_info[curr]:
            if repeat[curr][n]:
                continue
            repeat[curr][n] = True
            repeat[n][curr] = True
            children_info, temp_children_route = self.dfs(n, signal_speed, nodes_info, weights_info, repeat, res)
            # 当前节点连接 n 节点的权值
            weight = weights_info[curr][n]
            down_total_weights.append(weights_info[curr][n])

            # 记录子节点情况（记录 n 有几条符合条件的路径）
            route = 0
            # curr 节点和 n 节点的权值是否符合被 signal_speed 整除
            if weight % signal_speed == 0:
                res[curr] += 1
                route += 1
            # 将“curr 节点和 n 节点的权值（weight）”权值与子节点的权值相加，验证是否能够被 signal_speed 整除
            for child in children_info:
                if (weight + child) % signal_speed == 0:
                    res[curr] += 1
                    route += 1
                # 将子节点的权值与 weight 累加起来之后存储
                down_total_weights.append(weight + child)
            # 分别存储下 curr 下的所有子节点的所有符合条件的路径，children_route[i] 表示 第 i 个子节点下有这么多符合条件的路径
            if route > 0:
                children_route.append(route)

        return down_total_weights, children_route

    """
    返回图的信息（所有节点的连接情况）
    1、返回所有节点分别都连接到哪些节点
    2、返回所有两个连接点的权值
    """
    def get_map_info(self, edges: List[List[int]]):
        # key节点分连接value节点
        nodes_info = {}
        # 二维数组，两个连接节点的权值是多少
        weights_info = [[0] * (len(edges) + 1) for _ in range(len(edges) + 1)]
        for n in edges:
            # 权值信息加入 weights_info 中去
            weights_info[n[0]][n[1]] = n[2]
            weights_info[n[1]][n[0]] = n[2]
            # 节点连接信息加入 nodes_info 中去
            if n[0] in nodes_info:
                nodes_info[n[0]].append(n[1])
            else:
                nodes_info[n[0]] = [n[1]]

            if n[1] in nodes_info:
                nodes_info[n[1]].append(n[0])
            else:
                nodes_info[n[1]] = [n[0]]

        return nodes_info, weights_info

    # 节点全排序
    def count_pair_permutations(self, nums):
        total_permutations = 0
        n = len(nums)

        # 双重循环遍历所有元素对
        for i in range(n):
            for j in range(n):
                if i != j:
                    total_permutations += 1

        return total_permutations
#endregion

edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
signalSpeed = 1

edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
signalSpeed = 1

# edges = [[0,6,2],[6,7,2],[7,8,2],[6,5,1],[5,9,5],[5,10,2],[0,3,1],[3,1,2],[3,4,2],[3,2,7]]
# signalSpeed = 3

Solution3().countPairsOfConnectableServers(edges, signalSpeed)