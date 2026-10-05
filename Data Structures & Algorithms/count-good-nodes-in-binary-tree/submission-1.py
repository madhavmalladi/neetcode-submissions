# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # have an internal function that takes in a root and curr_max
        good_nodes = 0
        def is_good(root, curr_max) -> int:
            return_val = 0
            if root.val >= curr_max:
                return_val = 1
                curr_max = root.val
            
            if root.left:
                return_val += is_good(root.left, curr_max)
            if root.right:
                return_val += is_good(root.right, curr_max)

            
            return return_val
        
        return is_good(root, root.val)
            
            