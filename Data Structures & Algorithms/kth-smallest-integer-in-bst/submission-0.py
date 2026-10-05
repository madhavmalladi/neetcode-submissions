# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes_visited = 0

        def in_order_traverse(node) -> Optional[int]:
            if not node:
                return

            # check left child
            left_result = in_order_traverse(node.left)
            if left_result:
                return left_result
            
            # check current node
            self.nodes_visited += 1
            if self.nodes_visited == k:
                return node.val

            # check right node
            return in_order_traverse(node.right)

        return in_order_traverse(root)