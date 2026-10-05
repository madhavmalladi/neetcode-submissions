# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find where p.val <= root.val <= q.val
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                # current is too high
                current = current.left
            
            elif p.val > current.val and q.val > current.val:
                # current is too low
                current = current.right
            
            else:
                return current