# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, depth = [root], {None: 0}
        if root:
            while stack:
                node = stack[-1]
                if node.left and node.left not in depth:
                    stack.append(node.left)
                elif node.right and node.right not in depth:
                    stack.append(node.right)
                else:
                    stack.pop()
                    left, right = depth.get(node.left, 0), depth.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depth[node] = max(left, right) + 1
        return True
