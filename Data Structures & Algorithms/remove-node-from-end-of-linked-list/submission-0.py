# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        i = 0

        while head:
            if i >= n:
                prev = prev.next
            head = head.next
            i += 1

        prev.next = prev.next.next
        return dummy.next