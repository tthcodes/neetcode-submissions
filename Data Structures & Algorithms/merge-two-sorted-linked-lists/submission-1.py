# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # made a dummy node to cover the edge case 
        dummy = ListNode() 

        # set the moving tail to the dummy 
        tail = dummy 

        # while statement will be as long as both list1 and 2 are not None, so it can compare
        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2 
                tail = tail.next
                list2 = list2.next
            else:
                tail.next = list1
                tail = tail.next
                list1 = list1.next 
        
        if list1:
            tail.next = list1 
        else:
            tail.next = list2
        
        return dummy.next

                
