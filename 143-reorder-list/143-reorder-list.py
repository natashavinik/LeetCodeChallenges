# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr, prev = slow, None
        
        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        
        first, second = head, prev
        
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        
        
        