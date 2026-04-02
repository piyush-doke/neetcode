# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            stack, visited = [node], {None: "#"}
            while stack:
                n = stack[-1]
                if n.left and n.left not in visited:
                    stack.append(n.left)
                elif n.right and n.right not in visited:
                    stack.append(n.right)
                else:
                    stack.pop()
                    left = visited.get(n.left, "#")
                    right = visited.get(n.right, "#")
                    visited[n] = f"^{n.val},{left},{right}"
            return visited[node]

        return serialize(subRoot) in serialize(root)
