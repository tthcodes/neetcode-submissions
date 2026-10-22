# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    # need a merge sorted list helper 
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy 
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next 
        if list1:
            tail.next = list1 
        else:
            tail.next = list2 
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge cases for when there's no list length
        if not lists or len(lists) == 0:
            return None
        
        
        # now when lists have an actual length you want to loop through
        while len(lists) > 1:
            # merged lists var
            mergedLists = []
            # now we loop through the list 
            for i in range(0, len(lists), 2):
                # 2 step, and you grab first and 2nd list 
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(list1, list2))
            # reassign list to mergedLists
            lists = mergedLists # this is what allows the loop to ocntinue until all pairs are merged
        
        return mergedLists[0]
        