# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return head
        left = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return left
    def reorderList(self, head: ListNode | None) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        curr = head
        while rev.next is not None:
            tempcurr = curr.next
            curr.next = rev
            temprev = rev.next
            rev.next = tempcurr
            curr = tempcurr
            rev = temprev
        """
        Do not return anything, modify head in-place instead.
        """
        