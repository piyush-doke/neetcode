# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = [0]

        def dfs(node, largest):
            if node:
                if node.val >= largest: result[0] += 1
                dfs(node.left, max(largest, node.val))
                dfs(node.right, max(largest, node.val))

        dfs(root, float("-inf"))
        return result[0]
