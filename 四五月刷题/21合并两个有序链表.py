from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #将list1和list2分别转化为数组类型的
        array1 = [] if list1 is None else self.generate_list(list1)
        array2 = [] if list2 is None else self.generate_list(list2,[])

        merge_array = array1 + array2
        merge_array.sort()
        top_array_node = self.generate_node(merge_array, ListNode(), 0)
        return top_array_node.next

    #将ListNode的value转成数组类型的
    def generate_list(self,node:Optional[ListNode],array=[]):
        if node is not None:
            array.append(node.val)
            self.generate_list(node.next, array)
        return array

    #将数组转化成ListNode实例
    def generate_node(self,merge_array,parent_node,idx):
        if idx<len(merge_array):
            curr_node = self.generate_node(merge_array,ListNode(merge_array[idx]),idx+1)
            parent_node.next = curr_node
        return parent_node

if __name__ == '__main__':
    list_node1 = ListNode(1)
    next1 = ListNode(2)
    next2 = ListNode(4)

    next1.next = next2
    list_node1.next = next1


    list_node2 = ListNode(1)
    next3 = ListNode(3)
    next4 = ListNode(4)

    next3.next=next4
    list_node2.next=next3

    Solution().mergeTwoLists(list_node1,list_node2)