import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 序列化
    def serialize(self, root):
        if root is None:
            return '[]'
        nodes = [root]
        result = []
        while len(nodes) > 0:
            node = nodes[0]
            del nodes[0]
            if node is not None:
                result.append(node.val)
                left = node.left
                right = node.right
                nodes.append(left)
                nodes.append(right)
            else:
                result.append(None)
        # 会冗余很多的None，要为列表去除掉多余的None
        # 最后一个数字的索引位置
        last_num = next(((i + 1) for i in range(len(result) - 1, -1, -1) if isinstance(result[i], int)), None)
        result = result[:last_num:1]
        return "["+','.join(map(lambda n: str(n),result))+"]"

    # 反序列化
    def deserialize(self, data):
        if len(data) == 2:
            # 处理空的列表。'[]'
            return None
        ary = list(map(lambda n: None if n.upper() == 'NONE' else int(n), data[1:-1].split(',')))
        sun = self.sun_deserialize(ary, 0)
        return sun

    def sun_deserialize(self, data, curr_idx):
        val = data[curr_idx]
        if val is None:
            return None
        curr = TreeNode(data[curr_idx])
        # 当前索引*2+1-(before_null_num*2)//before_null_num：当前索引之前的null的数量
        left_idx = curr_idx * 2 + 1 - (len(list(filter(lambda n:n is None,data[:curr_idx:1]))) * 2)
        right_idx = curr_idx * 2 + 2 - (len(list(filter(lambda n:n is None,data[:curr_idx:1]))) * 2)
        if left_idx < len(data):
            left = self.sun_deserialize(data, left_idx)
            curr.left = left
        if right_idx < len(data):
            right = self.sun_deserialize(data, right_idx)
            curr.right = right
        return curr

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

root = TreeNode(1)
root.left = None
root.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)
root.right.right.left.left = TreeNode(8)
root.right.right.left.right = TreeNode(9)

root = TreeNode(1)
root.left = None
root.right = TreeNode(3)
root.right.left = TreeNode(6)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))