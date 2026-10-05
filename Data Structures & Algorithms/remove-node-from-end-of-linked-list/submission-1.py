# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # removal: node.next = node.next.next
        # 1 -> 2 -> 3 -> 4
        #      p1          -> p2
        # edge case: we need to remove the first node, so we need to start p1 at the position before the first node

        dummy = ListNode()
        dummy.next = head

        slow, fast = dummy, dummy
        for i in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        # now, slow is right before the node we need to remove
        slow.next = slow.next.next

        return dummy.next