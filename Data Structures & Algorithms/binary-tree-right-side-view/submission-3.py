# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we do a level order traversal and for each level, we append
        # curr_level[-1] to the answer array

        if not root:
            return []

        queue = deque()
        ans = []
        
        queue.append(root)

        while queue:
            level_length = len(queue)
            curr_level = []

            for i in range(level_length):
                current_node = queue.popleft()
                curr_level.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                
            ans.append(curr_level[-1])

        return ans
