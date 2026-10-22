# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # cycle = if one node in list can be visited again by following the 'next' pointer 
        memory = []

        curHead = head 

        while head:
            if not head.next:
                return False
            if head.val in memory:
                return True
            else:
                memory.append(head.val)
            
            head = head.next 
        
        return False