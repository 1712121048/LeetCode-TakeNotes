import copy
# class SnapshotArray:
#     # 初始化一个与指定长度相等的类数组的数据结构。初始时，每个元素都等于 0。
#     def __init__(self, length: int):
#         # 列表
#         self.shot_ary = [0] * length
#         # 快照字典
#         self.shot_dict = {}
#         # snap_id（snap() 的总次数）
#         self.amount = 0
#
#     # 会将指定索引 index 处的元素设置为 val。
#     def set(self, index: int, val: int) -> None:
#         self.shot_ary[index] = val
#
#     # 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
#     def snap(self) -> int:
#         self.amount += 1
#         self.shot_dict[self.amount - 1] = copy.copy(self.shot_ary)
#         return self.amount - 1
#
#     #  根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
#     def get(self, index: int, snap_id: int) -> int:
#         return self.shot_dict[snap_id][index]
import collections
class SnapshotArray:
    # 初始化一个与指定长度相等的类数组的数据结构。初始时，每个元素都等于 0。
    def __init__(self, length: int):
        # set的历史记录。（快照索引，set值）
        self. history = collections.defaultdict(list) #[[()]]
        # snap_id（snap() 的总次数）
        self.amount = 0

    # 会将指定索引 index 处的元素设置为 val。
    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.amount, val))

    # 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。
    def snap(self) -> int:
        self.amount += 1
        return self.amount - 1

    #  根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。
    def get(self, index: int, snap_id: int) -> int:
        # 可以考虑使用bisect的bisect_left方法。bisect.bisect_left(self.history[index], (snap_id + 1,)) - 1
        # 返回返回大于等于snap_id+1的第一个下标。
        # 一个有序列表，我们的目标是要获取到大于等于snap_id的最后一个。也就说要获取第一个snap_id+1的后面的第一个。也就是bisect_left(self.history[index], (snap_id + 1,))要“-1”的原因。
        left = 0
        right = len(self.history[index])
        sun = 0
        while left < right:
            sun = (left + right) // 2
            if self.history[index][sun][0] < snap_id + 1:
                left = sun + 1
            else:
                right = sun
        sun = left - 1
        if sun < 0:
            return 0
        else:
            return self.history[index][sun][1]


# obj = SnapshotArray(31)
# obj.set(0,5)
# param_2 = obj.snap()
# obj.set(0,6)
# param_3 = obj.get(0,0)
# obj.set(9,999)
# param_2 = obj.snap()
# obj.set(9,9999)
# param_3 = obj.get(9,0)

# obj = SnapshotArray(10000)
# obj.set(0,381)
# param_2 = obj.snap()
# obj.get(0,0)

obj = SnapshotArray(13)
obj.set(0,5)
param_2 = obj.snap()
param_2 = obj.snap()
obj.set(0,6)
obj.get(0,0)