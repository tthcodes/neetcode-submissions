# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make adummy node as a beginning
        dummy = ListNode()
        
        # init a tail and set it to dummy so it moves
        tail = dummy

        # while loop for when list1 and list2 both NOT none
        while list1 and list2:
            # compare 
            if list2.val <= list1.val:
                # want tail to point to list2 
                tail.next = list2 
                # update list2 to move along
                list2 = list2.next 
            else:
                tail.next = list1
                list1 = list1.next 
            tail = tail.next
        
        if not list2:
            tail.next = list1 
        
        else:
            tail.next = list2
        
        return dummy.next
