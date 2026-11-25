# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return left
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        curr = head
        prev = None
        carry = 0
        while curr is not None:
            newValue = curr.val * 2 + carry
            curr.val = newValue % 10
            if newValue >= 10:
                carry = 1
            else:
                carry = 0
            prev = curr
            curr = curr.next
        if carry != 0:
            newHead = ListNode(carry)
            prev.next = newHead
        return self.reverse(head)
        