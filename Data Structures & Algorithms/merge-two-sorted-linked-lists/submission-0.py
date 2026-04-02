# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, list1)
        head1 = list1
        head2 = list2
        
        while head1 or head2:
            if head1 and head2:
                if head1.val < head2.val:
                    prev = head1
                    head1 = head1.next
                else:
                    prev.next = head2
                    temp = head2.next
                    head2.next = head1
                    prev = head2
                    head2 = temp
            else:
                if head2:
                    prev.next = head2
                break


        return dummy.next