# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal and return arr[k-1]
        arr = []

        def in_order_traverse(root):
            if not root:
                return
            
            in_order_traverse(root.left)
            arr.append(root.val)
            in_order_traverse(root.right)

        in_order_traverse(root)
        return arr[k-1]