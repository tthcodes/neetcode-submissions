# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we can create a dummy node here to start things off. then we always have a ref to head
        dummy = ListNode()
        # then a tail to start from dummy
        tail = dummy 
        # tricky part here to me is the lists being different lengths 
        while list1 and list2: # this makes sure both lists are not at end/none to even compare
            if list1.val >= list2.val:
                # if list2  begins lower or same, set tail there 
                tail.next = list2
                # move list2 along
                list2 = list2.next 
                # move tail along
                tail = tail.next
            else: # else if list1 is greater
                tail.next = list1 
                list1 = list1.next 
                tail = tail.next

        
        # else if one of them no longer exists, move tail to the other and return head
        if list1:
            tail.next = list1 
        else:
            tail.next = list2
        
        return dummy.next