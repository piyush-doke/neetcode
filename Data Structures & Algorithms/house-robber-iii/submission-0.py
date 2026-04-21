# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # def rc(node):
        #     rcl_with, rcl_without = rc(node.left)
        #     rcl_with, rcl_without = rc(node.left)
        #     without_node = 
        #     with_node = 
        #     return [with_node, without_node]
        
        def shreyas(node):
            if node:
                l_rob, l_not_rob = shreyas(node.left)
                r_rob, r_not_rob = shreyas(node.right)
                return node.val + l_not_rob + r_not_rob, max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return 0, 0
        
        a, b = shreyas(root)
        return max(a, b)