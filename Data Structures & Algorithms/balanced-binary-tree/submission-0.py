# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calculate left and right lengths for every node and see
        # if they differ by no more than 1

        def dfs(root) -> tuple[bool, int]:
            if not root:
                return [True, 0]
            
            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)

            height = 1 + max(left_height, right_height)
            balanced = (left_balanced and right_balanced
            and (abs(left_height - right_height) <= 1))

            return [balanced, height]
        

        return dfs(root)[0]        
