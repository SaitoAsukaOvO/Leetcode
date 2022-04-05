# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        '''
        claim 3 Vars: prev, cur, next

        None --> 1 --> 2 --> 3 --> 4 --> 5
        prev    cur   next

        None <-- 1    2 --> 3 --> 4 --> 5
        prev    cur   next

        Move the three vars:
        None <-- 1    2 --> 3 --> 4 --> 5
                prev  cur   next

         None <-- 1 <--2     3 --> 4 --> 5
                prev  cur   next
        '''

        prev = None
        cur = head
        while cur:
            nxt = cur.next
            # flip next
            cur.next = prev
            # move the three vars
            prev = cur
            cur = nxt
        return prev
