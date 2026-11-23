# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1, p2 = None, None
        temp = head
        while temp is not None:
            if p2 is not None:
                p2 = p2.next
            k-= 1
            if k == 0:
                p1 = temp
                p2 = head
            temp = temp.next
        p1.val, p2.val = p2.val, p1.val
        return head
        