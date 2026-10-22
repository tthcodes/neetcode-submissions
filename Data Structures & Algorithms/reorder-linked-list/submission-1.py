# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to determine the MIDDLE of list using fast/slow pointers 
        fast, slow = head.next, head 
        # starting them on different nodes, with fast being one ahead, SHOULD move it so it hits end and slow is midpoint

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # at this point slow is either middle element, which we can include as first half or it's end of first half
        # we need to disconnect first half from second half 
        rightHead = slow.next
        slow.next = None 

        # now we can reverse the second half, using SLOW as our midpoint
        # establish prevNode 
        prevNode = None
        while rightHead:
            # grab rightHead's next
            nextNode = rightHead.next 
            # righthead's next should be prevNode 
            rightHead.next = prevNode 
            # not change prevNode to this node
            prevNode = rightHead 
            # change righthead to next 
            rightHead = nextNode

        # now righthead's next should be the head of reversed 2nd half
        # now you interweave, WHILE rightHead still exists
        rightHead = prevNode
        leftHead = head

        while rightHead:
            #HOLD the next nodes for left and right
            nextLeft = leftHead.next
            nextRight = rightHead.next

            # now we want to link the leftHead to rightHead
            leftHead.next = rightHead 
            # now we link rightHead's next to next left 
            rightHead.next = nextLeft 

            # NOW we re-establish the left and right heads to MOVE ALONG
            leftHead = nextLeft
            rightHead = nextRight


