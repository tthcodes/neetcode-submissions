# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start with base case, ends with NOne
        if head == None:
            return None
        
        # we want to set input head as current head for now
        curHead = head 

        # we want to check if it has a next, if so we want to set next to this one
        if head.next:
            # if there is a NEXT, we want to run reverseList and result is now curHead
            curHead = self.reverseList(head.next) # so we perform it on next node
            head.next.next = head
        
        # after reversal, we break the pointer 
        head.next = None
        
        return curHead