# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         normal = dummy
#         fast = head
        
#         while n >0 and fast:
#             fast = fast.next
#             n -= 1
#             print(n)
#         while fast and fast.next:
#             normal = normal.next
#             fast = fast.next
#         normal.next = normal.next.next
#         return dummy.next
    
    
    
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        while n != 0 and fast:
            fast = fast.next
            n -= 1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        
        return dummy.next
    
        
            
            
    
            
      
    
    