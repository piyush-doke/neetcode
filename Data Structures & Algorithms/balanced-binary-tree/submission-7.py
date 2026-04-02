# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            if not root or not balanced: return 0
            left, right = maxDepth(root.left), maxDepth(root.right)
            if balanced:
                balanced = (abs(left - right) <= 1)
            return max(left, right) + 1

        maxDepth(root)
        return balanced