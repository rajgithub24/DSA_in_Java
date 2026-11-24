# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small = ListNode(0)
        large = ListNode(0)
        smallP = small
        largeP = large
        while head is not None:
            if head.val < x:
                smallP.next = head
                smallP = smallP.next
            else:
                largeP.next = head
                largeP = largeP.next

            head = head.next
        smallP.next = large.next
        largeP.next = None
        return small.next
        