from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # 处理单个节点的
        if root.left is None and root.right is None:
            return 0
        # 序列换完成的二叉树，可以根据索引区分是左节点还是右节点。（奇左偶右）
        root_list = [root.val]
        # 索引：（父索引，当前索引的value,之前的None数量）
        temp = {0: (0, root.val, 0)}
        # 值-索引
        temp2 = {}
        # 存储每个节点的父节点
        child_parent = {}
        # 序列化二叉树
        def serialize(tree: Optional[TreeNode]):
            # bfs序列化二叉树
            nonlocal root_list
            nodes = [tree]
            parent_idx = 0
            # None数量
            null_amout = 0
            index = 0
            while len(nodes) > 0:
                node = nodes[0]
                del nodes[0]
                if node is not None:
                    left = node.left
                    right = node.right
                    nodes.append(left)
                    nodes.append(right)
                    temp2[node.val] = index
                    temp[index] = (parent_idx, node.val, null_amout)
                    if left is not None:
                        root_list.append(left.val)
                        child_parent[left.val] = node.val
                    else:
                        root_list.append(None)

                    if right is not None:
                        root_list.append(right.val)
                        child_parent[right.val] = node.val
                    else:
                        root_list.append(None)
                else:
                    temp[index] = (parent_idx, None, null_amout)
                    null_amout += 1
                index += 1
            last_num = next(((i + 1) for i in range(len(root_list) - 1, -1, -1) if isinstance(root_list[i], int)), None)
            root_list = root_list[:last_num]
        serialize(root)
        inf_idx = root_list.index(start)
        # 最新感染序列
        inf_queue = deque()
        inf_queue.append(inf_idx)
        # 节点索引映射节点级别，记录所有原发节点
        idx_level = { inf_idx: 0 }
        #结果
        result = 0
        lst_len = len(root_list)
        # 宽搜
        while inf_queue:
            node_idx = inf_queue.popleft()
            node_level = idx_level[node_idx]
            # before_null_num：当前索引之前的null的数量
            before_null_num = temp[node_idx][2]  # temp[node_idx][2]

            # 当前节点的父节点索引
            parent_idx = -1
            if node_idx == 0:
                # 根节点没有父节点
                parent_idx = 0
            else:
                # 使用存下来的父子关系映射字典
                parent_idx = temp2[child_parent[root_list[node_idx]]]

            if parent_idx not in idx_level:
                # 记录父节点
                inf_queue.append(parent_idx)
                idx_level[parent_idx] = node_level + 1

            # 左右子节点计算公式：
            # 左：当前索引×2 + 1 - (before_null_num×2)
            # 右：当前索引×2 + 2 - (before_null_num×2)
            left = node_idx * 2 + 1 - (before_null_num * 2)
            right = node_idx * 2 + 2 - (before_null_num * 2)

            # 将新感染的存入（左子）
            if left < lst_len and temp[left][1] is not None and left not in idx_level:
                # 记录左子节点
                inf_queue.append(left)
                idx_level[left] = node_level + 1
            # 将新感染的存入（右子）
            if right < lst_len and temp[right][1] is not None and right not in idx_level:
                # 记录右子节点
                inf_queue.append(right)
                idx_level[right] = node_level + 1
            result = node_level
        return result

    # 获取感染整个root_list最少需要多长时间
    def get_infect_date(self,root_data:list, inf_flag:list, child_parent,level = 1):
        # 已感染节点索引
        infect_idxs = set([i for i, n in enumerate(inf_flag) if n == 1])
        # 模拟扩散当前感染源
        for n in infect_idxs:
            # before_null_num：当前索引之前的null的数量
            before_null_num = root_data[:n].count(None)
            # 当前节点的父节点索引
            parent_idx = -1
            if n == 0:
                # 根节点没有父节点
                parent_idx = 0
            else:
                # # 父节点的计算方式
                # # 奇左偶右
                #parent_idx = (n - 2 + root_data[:n-1].count(None) * 2) // 2 if n % 2 == 0 else (n - 1 + before_null_num * 2) // 2
                # 使用存下来的父子关系映射字典
                parent_idx = root_data.index(child_parent[root_data[n]])
            # 将新感染的存入（父）
            if inf_flag[parent_idx] == 0:
                # 更新节点状态
                inf_flag[parent_idx] = 1
            # 左右子节点计算公式：
            # 左：当前索引×2 + 1 - (before_null_num×2)
            # 右：当前索引×2 + 2 - (before_null_num×2)
            left = n * 2 + 1 - (before_null_num * 2)
            right = n * 2 + 2 - (before_null_num * 2)
            # 将新感染的存入（左子）
            if left < len(inf_flag) and inf_flag[left] == 0:
                # 更新节点状态
                inf_flag[left] = 1
            # 将新感染的存入（右子）
            if right < len(inf_flag) and inf_flag[right] == 0:
                # 更新节点状态
                inf_flag[right] = 1
        if 0 in set(inf_flag):
            return self.get_infect_date(root_data, inf_flag, level + 1)
        else:
            return level


# [1,null,3,null,5,6,7,8,9]
root = TreeNode(1)
root.left = None
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root.right.right.left.left = TreeNode(8)
root.right.right.left.right = TreeNode(9)
start = 7

# [1,5,3,null,4,10,6,9,2]
root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(3)
root.left.left = None
root.left.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(2)
start = 3

# # [1]
# root = TreeNode(1)
# start = 1
#
# # [1,2]
# root = TreeNode(1)
# root.right = TreeNode(2)
# start = 2
#
# # [3,1,4,null,null,2]
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)
# start = 2

Solution().amountOfTime(root,start)