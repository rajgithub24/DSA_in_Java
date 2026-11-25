# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        head = head.next
        if head is None:
            return head
        sum = 0
        temp = head
        while temp is not None and temp.val != 0:
            sum+= temp.val
            temp = temp.next
        head.val = sum
        head.next = self.mergeNodes(temp)
        return head
        
        