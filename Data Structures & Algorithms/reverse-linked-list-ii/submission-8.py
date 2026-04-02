# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)

        for _ in range(left - 1):
            prev, head = head, head.next
        
        tail, curr = head, head.next
        for _ in range(right - left):
            curr.next, head, curr = head, curr, curr.next
        
        tail.next, prev.next = curr, head

        return dummy.next