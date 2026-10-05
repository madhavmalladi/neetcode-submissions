# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # sum of the heights of root.left and root.right
        self.max_diameter = 0
        def calculateHeight(root) -> int:
            if not root:
                return 0
        
            leftHeight = calculateHeight(root.left)
            rightHeight = calculateHeight(root.right)

            diameter = leftHeight + rightHeight
            self.max_diameter = max(self.max_diameter, diameter)

            return 1 + max(leftHeight, rightHeight)
        
        calculateHeight(root)
        return self.max_diameter