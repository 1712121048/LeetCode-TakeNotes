from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = self.node_convert_array(head,[])
        array_swap = self.array_exchange(array)
        node = self.create_node(ListNode(),array_swap,0)
        return node.next

    #将ListNode的val按照顺序拿出来
    def node_convert_array(self, head: Optional[ListNode],array=[]) -> Optional[list]:
        if head is not None:
            array.append(head.val)
            self.node_convert_array(head.next,array)
        return array

    #对数组进行位置交换
    def array_exchange(self,array) -> Optional[list]:
        range_list = list(range(len(array)))
        new_array=list()
        for i in range_list:
            if i % 2 == 0:
                if i + 1 <= max(range_list):
                    new_array.append(array[i+1])
                    new_array.append(array[i])
                else:
                    new_array.append(array[i])
        return new_array

    #将数组转化为ListNode类型的
    def create_node(self, parent_node, array, idx):
        if idx < len(array):
            curr_node = self.create_node(ListNode(array[idx]),array,idx+1)
            parent_node.next = curr_node
        return parent_node


if __name__ == '__main__':
    Solution().swapPairs(ListNode(1,None))