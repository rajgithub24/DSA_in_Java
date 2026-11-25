# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set(nums)
        dummy = ListNode(0)
        curr = dummy
        while head is not None:
            if head.val not in seen:
                curr.next = head
                curr = curr.next
            head = head.next
        
        curr.next = None
        return dummy.next