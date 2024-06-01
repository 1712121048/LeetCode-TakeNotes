from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         self.big = 0
class Solution:
    def maxPathSum(self) -> int:
        root = TreeNode(-10,TreeNode(9,None,None),TreeNode(20,TreeNode(15),TreeNode(7)))
        root = TreeNode(1,TreeNode(-2),TreeNode(3))
        result = self.maxPathSum2(root,-1001)
        return result[-1]

    def maxPathSum2(self, root, record = -1001):
        if root is None:
            return -1001,record
        left_val, temp1 = self.maxPathSum2(root.left,record)
        right_val, temp2 = self.maxPathSum2(root.right,record)
        record = max(record,temp1,temp2)
        root.big = max(root.val, max(left_val, right_val) + root.val)
        left_val = 0 if left_val == -1001 else left_val
        right_val = 0 if right_val == -1001 else right_val
        root.val = root.val + left_val + right_val
        record = max(root.big,root.val,record)
        return root.big,record

Solution().maxPathSum()