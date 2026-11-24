# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        ptr = temp = head
        for _ in range(n):
            ptr = ptr.next
            
        if ptr is None:
            return head.next
            
        while ptr.next is not None:
            ptr = ptr.next
            temp = temp.next
            
        temp.next = temp.next.next
        return head
        