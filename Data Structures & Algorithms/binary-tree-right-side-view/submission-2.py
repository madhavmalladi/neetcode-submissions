# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        ans = []

        queue.append(root)

        while queue:
            level_size = len(queue)
            right_most_node = -101

            for i in range(level_size):
                right_most_node = queue.popleft()

                if right_most_node.left:
                    queue.append(right_most_node.left)

                if right_most_node.right:
                    queue.append(right_most_node.right)
            
            ans.append(right_most_node.val)

        return ans