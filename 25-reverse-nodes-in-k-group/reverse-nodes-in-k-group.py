# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        t = head
        n = 0
        while t:
            t = t.next 
            n += 1
        lim = (n//k ) * k
        temp = head
        prev_rev = dummy
        trav = 1
        while trav < lim:
            prev = temp
            temp = temp.next
            prev.next = None
            trav += 1
            for _ in range(k-1):
                Next = temp.next
                temp.next = prev
                prev = temp
                temp = Next
                trav += 1
            prev1 = prev_rev.next
            prev_rev.next.next = temp
            prev_rev.next = prev
            prev_rev = prev1

        return dummy.next