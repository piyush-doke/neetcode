# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path = [float("-inf")]
        
        def dfs(node):
            if node:
                left = max(dfs(node.left), 0)
                right = max(dfs(node.right), 0)
                path[0] = max(path[0], left + right + node.val)
                return node.val + max(left, right)
            return 0

        dfs(root)
        return path[0]