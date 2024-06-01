from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        root.flag = 0
        result = 0
        # -1：无需监控，0：未监控，1：父监控，2：子监控，3：亲自监控
        def dfs(node, n) -> int:
            if node is None:
                return -1
            nonlocal result
            node.flag = 0
            left_child_flag = dfs(node.left, n+1)
            right_child_flag = dfs(node.right, n+1)

            # 最低层
            if left_child_flag == -1 and right_child_flag == -1:
                return 0
            # 存在一个未被覆盖的子节点。亲自监控
            elif left_child_flag == 0 or right_child_flag == 0:
                result += 1
                return 3
            # 不存在未被监控的子节点。且子节点当中存在这一个 ”亲自监控“
            elif left_child_flag == 3 or right_child_flag == 3:
                return 2
            else:
                # 根节点
                if n == 0:
                    result += 1
                # 子节点被孙节点监控
                return 0
        dfs(root, 0)
        # 处理单个节点。[0]
        result = max(result, 1)
        return result

# [0,0,0,0,null,0,0,0,0,null,null,0,0,0,0]
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(0)
root.right.right.left = TreeNode(0)
root.right.right.right = TreeNode(0)
root.left.left.left.left = TreeNode(0)
root.left.left.left.right = TreeNode(0)

# [0,null,0,null,0,null,0]
root = TreeNode(0)
root.right = TreeNode(0)
root.right.right = TreeNode(0)
root.right.right.right = TreeNode(0)
root.right.right.right.right = TreeNode(0)
Solution().minCameraCover(root)