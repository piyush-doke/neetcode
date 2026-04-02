# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        total = 0

        while l1 or l2 or total:
            if not l1 and not l2 and total:
                l1 = p1.next = ListNode()
            if not l1 and l2:
                l1 = p1.next = l2
                l2 = p2.next = None

            if l1:
                total += l1.val
                p1, l1 = l1, l1.next
            if l2:
                total += l2.val
                p2, l2 = l2, l2.next
            total, p1.val = divmod(total, 10)

        return head