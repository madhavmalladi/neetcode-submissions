# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            nextN = current.next
            current.next = prev
            prev = current
            current = nextN
        
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3] | [4, 5, 6]
            # - do this using a slow and fast pointer
        # next, call reverse_list() on the second half, which is the slow pointer
        # then begin merging

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        ptr1 = head
        ptr2 = self.reverse_list(second)

        while ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr2.next = temp1
            ptr1.next = ptr2
            ptr2 = temp2
            ptr1 = temp1
        


