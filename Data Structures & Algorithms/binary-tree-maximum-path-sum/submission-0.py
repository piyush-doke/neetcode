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
                left, right = dfs(node.left), dfs(node.right)
                path[0] = max(path[0], max(left, 0) + max(right, 0) + node.val)
                return node.val + max(max(left, right), 0)
            return 0

        dfs(root)
        return path[0]