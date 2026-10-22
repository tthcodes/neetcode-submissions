# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iterative approach 
        # prevNode = None

        # curNode = head

        # while curNode:
        #     # keep hold of next 
        #     nextNode = curNode.next 
        #     # change current next to previous
        #     curNode.next = prevNode 
        #     # update prevNode to be this node
        #     prevNode = curNode 
        #     # update curNode to next 
        #     curNode = nextNode 
        
        # # since it stops when you reach the end, the previous node is now the new head
        # return prevNode

        if not head:
            return None
        
        newHead = head 

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead