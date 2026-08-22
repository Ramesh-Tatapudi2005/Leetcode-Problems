# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        t = head
        pre = dummy
        while t:
            if t.val == val:
                pre.next = t.next
                t = t.next
            else:
                pre = t
                t = t.next if t else None
        return dummy.next