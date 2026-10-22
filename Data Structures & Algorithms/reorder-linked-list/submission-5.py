# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we need to remember the three steps, split, reverse, weave.
        # we need to also remember the proper fast and slow boundaries and starting points. starting fast 1 step ahead guarantees slow is always at the end of 1st half, with 1st half being the bigger half at odd lenghts

        #init slow and fast
        slow, fast = head, head.next 

        # we want to loop it as long as fast and fast.next exist
        while fast and fast.next: # this allows fast to land on none.
            slow = slow.next 
            fast = fast.next.next 

        # now it's stopped, and slow is the end of 1st half. now we want to disconnect. but before you do that, save the head2 as beginning of 2nd half. 
        head2 = slow.next
        slow.next = None

        # now head is the beginning of 1st half. now we reverse 2nd half. 
        prev = None 
        while head2:
            next = head2.next 
            head2.next = prev 
            prev = head2 
            head2 = next 

        # now prev will be the head of reverse order 2nd half 
        head2 = prev 
        head1 = head
        # now we interweave 
        while head1 and head2:
            temp = head1.next 
            temp2 = head2.next
            head1.next = head2 
            head2.next = temp 
            head1 = temp 
            head2 = temp2 