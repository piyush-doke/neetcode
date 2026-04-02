# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()
        
        while True:
            index, smallest = -1, float("inf")
            for i in range(len(lists)):
                if lists[i] and lists[i].val < smallest:
                    index, smallest = i, lists[i].val

            if index == -1:
                break

            head.next, lists[index] = lists[index], lists[index].next
            head = head.next
        
        return dummy.next