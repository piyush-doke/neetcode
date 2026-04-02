# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            m, n = stack.pop()
            if not m and not n: continue
            if not m or not n: return False
            if m.val != n.val: return False
            stack.append((m.left, n.left))
            stack.append((m.right, n.right))
        return True