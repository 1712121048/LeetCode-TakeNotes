from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = self.node_convert_array(head,[])
        new_array = self.array_exchange(array,k)
        node = self.array_convert_node(new_array,ListNode(),0)
        return node.next

    #提取ListNode的val为数组
    def node_convert_array(self, node: Optional[ListNode], array:Optional[list]):
        if node is not None:
            array.append(node.val)
            self.node_convert_array(node.next,array)
        return array

    #将每k个节点分为一组然后进行翻转，k的整倍数以外的节点顺序不变。
    def array_exchange(self, array:Optional[list], k:Optional[int]):
        mul = int(len(array)/k)
        stop = mul*k
        new_array=array[:stop]
        for m in range(mul):
            start = m*k
            end = start+k
            new_array[start:end] = new_array[start:end][::-1]
        new_array.extend(array[stop:])
        return new_array

    #将数组转化为ListNode类型
    def array_convert_node(self,array,parent_node,idx):
        if idx<len(array):
            curr_node = self.array_convert_node(array,ListNode(array[idx]),idx+1)
            parent_node.next = curr_node
        return parent_node

Solution().reverseKGroup(None,0)