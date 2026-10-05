# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6]
        # [0, 1, 2, 3] [4, 5, 6]
        # [0, 1, 2, 3] [6, 5, 4]
        # [0, 6, 1, 5, 2, 4, 3]

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        ptr2 = self.reverse_list(slow.next)
        slow.next = None
        ptr1 = head

        while ptr1 and ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1
            ptr1 = temp1
            ptr2 = temp2

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        nextN = head

        while current:
            nextN = current.next
            current.next = prev
            prev = current
            current = nextN
        
        return prev

