# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # have an internal function that takes (root, min, max)
        # min is the smallest possible value the node could have 
        # for it to be valid. max is the largest possible

        def is_valid(root, min_val, max_val):
            valid = False
            if min_val < root.val < max_val:
                valid = True
            
            if root.left:
                valid = valid and is_valid(root.left, min_val, root.val)
            if root.right:
                valid = valid and is_valid(root.right, root.val, max_val)
            return valid
        
        return is_valid(root, float('-inf'), float('inf'))