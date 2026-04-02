# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()

        heap = [(h.val, i, h) for i, h in enumerate(lists) if h]
        heapq.heapify(heap)

        while heap:
            val, i, node = heapq.heappop(heap)
            head.next = head = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next