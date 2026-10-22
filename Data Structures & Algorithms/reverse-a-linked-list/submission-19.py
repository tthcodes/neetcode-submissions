# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # we're going to account for if we're at the LAST or the EMPTY 
        # if not head or not head.next:
        #     return head 
        
        # # now we will invoke the recursion
        # newHead = self.reverseList(head.next) # we pass in the next to move it along

        # # now we have to implement the actual action of reversing each newHEad
        # head.next.next = head # set next head to current 
        # head.next = None # disconnect current next 

        # #now we trust newHead is the LAST NODE after reversing 
        # return newHead 
        prevNode = None 

        curHead = head

        while curHead:
            nextNode = curHead.next 
            curHead.next = prevNode 
            prevNode = curHead 
            curHead = nextNode 
        
        return prevNode