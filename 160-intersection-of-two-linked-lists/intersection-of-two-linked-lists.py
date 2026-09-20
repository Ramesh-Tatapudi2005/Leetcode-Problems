# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        Set = set()
        t = headA
        while t != None:
            Set.add(t)
            t= t.next
        t = headB
        while t  !=  None:
            if t in Set:
                return t
            t = t.next 
        return None