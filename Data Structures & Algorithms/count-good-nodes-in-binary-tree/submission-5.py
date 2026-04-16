# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([(root, float("-inf"))] if root else [])
        count = 0
        while q:
            node, largest = q.popleft()
            largest = max(largest, node.val)
            if node.val >= largest: count += 1
            if node.left: q.append((node.left, largest))
            if node.right: q.append((node.right, largest))
        return count