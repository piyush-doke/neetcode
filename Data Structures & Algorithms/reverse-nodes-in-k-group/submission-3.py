# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group_prev = dummy = ListNode(0, head)

        while True:
            # Find kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next

            # Reverse the group
            curr, prev = group_prev.next, group_next
            while curr != group_next:
                curr.next, curr, prev = prev, curr.next, curr

            group_prev.next, group_prev = prev, group_prev.next