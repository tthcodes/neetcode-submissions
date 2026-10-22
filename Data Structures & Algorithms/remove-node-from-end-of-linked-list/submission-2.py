# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node to hold onto head, also
        # lets you allow left and right to not be on actual removed node
        dummy = ListNode(0, head)
        # use two pointers so that you can detach node
        l, r = dummy, dummy 
        # start them at dummy. you want space between l and r to be N. 
        # then once the space is at N, you can to move both until r is at none
        while n >= 0:
            r = r.next 
            n -= 1
        
        # now that space between l, r = n, start moving both till r at end
        while r:
            r = r.next 
            l = l.next 
        
        # now that r is at the NONE, we know l is at the node BEFORE removal 
        l.next = l.next.next 

        return dummy.next
            