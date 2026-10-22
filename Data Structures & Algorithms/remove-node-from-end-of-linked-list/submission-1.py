# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # how do we get a sense for the total LENGTH of the linked list if we're removing from end?
        # maybe iterate through and just get a count, then reverse engineer it? 
        curNode = head 
        l = 0
        while curNode:
            l += 1
            curNode = curNode.next 
        if l == 1 and n == 1:
            return None
        # length - n = index of the node that needs to be removed 
        removeI = l - n 
        curNode = head 
        # scenario where the head is the one that needs to be removed, cut it and return next node
        if removeI == 0:
            newHead = curNode.next 
            curNode.next = None 
            return newHead
        # NEEd to keep a prevNode so that the node after curNode being removed can attach to it
        prevNode = None
        curNode = head 
        # not reset curNode to head and then when removeI = 0, we know we're on the node that needs to be removed
        while curNode and removeI > 0:
            prevNode = curNode 
            curNode = curNode.next 
            removeI -= 1
        prevNode.next = curNode.next 
        curNode.next = None 
        return head
        
