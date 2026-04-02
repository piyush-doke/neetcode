# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        
        def depth(node):
            if not node: return 0
            left, right = depth(node.left), depth(node.right)
            result[0] = max(result[0], left + right)
            return max(left, right) + 1
        
        depth(root)
        return result[0]