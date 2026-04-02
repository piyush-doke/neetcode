# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        depth = {None: 0}
        diameter = 0
        while stack:
            node = stack[-1]
            if node.left and node.left not in depth: stack.append(node.left)
            elif node.right and node.right not in depth: stack.append(node.right)
            else:
                stack.pop()
                depth[node] = max(depth[node.left], depth[node.right]) + 1
                diameter = max(diameter, depth[node.left] + depth[node.right])
        return diameter