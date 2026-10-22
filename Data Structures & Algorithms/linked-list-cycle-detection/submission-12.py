# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointers 

        fast, slow = head, head 

        while fast and fast.next: # while fast and fast.next are NOT null, since we'll shift fast by 2
            # move fast by 2, and slow by 1 
            slow = slow.next
            fast = fast.next.next 

            if slow == fast: # if they ever become the same, we know it's a cycle and this is O(n) time
                return True

        # else of loop breaks, we know fast eventually reached null and so did slow, it's not cycling
        return False

