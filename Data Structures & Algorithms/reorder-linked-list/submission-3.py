# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # three overall steps: split, reverse, interweave 
        # split by finding middle and breaking, using fast,slow 
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # now slow is in the middle, split, treat as slow as end of firstListNode
        # one thing triping me is how to handle odd lengths, 
        # what happens if first or second list longer than the other,
        # how do i handle that? whichever slow is a part of, it'll be longer.
        # does it matter?
        firstList = head 
        secondList = slow # this means second list longer 

        # now to reverse second list.
        prevNode = None 
        while secondList:
            nextNode = secondList.next 
            secondList.next = prevNode 
            prevNode = secondList 
            secondList = nextNode 
        # now prevNode is the head of secondList
        secondList = prevNode 

        # now we interweave 
        while firstList and secondList: # because secondList is the longer one .. ? should i do while both?
            # keep next for each list 
            nextFirst = firstList.next
            nextSecond = secondList.next 

            # now we do the new connections 
            firstList.next = secondList 
            secondList.next = nextFirst 

            # re-establish nexts
            secondList = nextSecond
            firstList = nextFirst 
        

