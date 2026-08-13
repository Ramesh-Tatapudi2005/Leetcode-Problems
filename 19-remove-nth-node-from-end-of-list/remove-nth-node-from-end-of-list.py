# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        m =0
        while t:
            m += 1
            t = t.next
        if n == m:
            return head.next
        temp = head
        while m != n + 1:
            temp = temp.next
            m -= 1
        temp.next = temp.next.next
        return head