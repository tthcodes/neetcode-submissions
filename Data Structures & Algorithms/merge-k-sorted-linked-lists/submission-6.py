# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
                # given an array of K linked lists lists, each LL sorted in ASCENDING ORDER,
        # merge all LLs into one sorted LLs and return it in ascending order. just return head

        # each ListNode has .val and .next 
        # nums can be negative. max sum of length is not over 10,000

        if not lists:
            return None

        # think we can do a helper function to merge 
        def merge(list1, list2):
            # this will merge the existing list and the next list. 
            # return the head of the merged list. 
            tempHead = ListNode()
            curr = tempHead
            while list1 and list2:
                if list1.val >= list2.val:
                    curr.next = list2
                    list2 = list2.next 
                else:
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next
            # now one of the lists have run out, connect end to rest of surviver
            if list1:
                curr.next = list1 
            else:
                curr.next = list2
            return tempHead.next


        # we need to loop through the list as long as there are any in lists.
        # what i'm having trouble with is how do we grab 2 lists at a time, while also guarding
        # against when it runs out? 

        head = ListNode()  # begin head at empty list node, then use curr to walk down each?

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(merge(list1, list2))
            lists = mergedLists

        return lists[0]

