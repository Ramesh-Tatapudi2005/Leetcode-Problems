# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0
        # t1 = l1
        # t2 = l2
        while l1 or l2:
            if l1 and l2:
                add = l1.val + l2.val + carry 
                curval = add % 10
                carry = add // 10
                newnode = ListNode(curval)
                if not head:
                    head = newnode
                    tail = newnode
                else:
                    tail.next = newnode
                    tail = newnode
                l1 , l2=  l1.next, l2.next
            elif l1:
                add = l1.val + carry 
                curval = add % 10 
                carry = add // 10
                newnode = ListNode(curval)
                if not head:
                    head = newnode
                    tail = newnode
                else:
                    tail.next  = newnode
                    tail = newnode
                l1 = l1.next
            else:
                add = l2.val + carry 
                curval = add % 10 
                carry = add // 10
                newnode = ListNode(curval)
                if not head:
                    head = newnode
                    tail = newnode
                else:
                    tail.next  = newnode
                    tail = newnode
                l2 = l2.next
        if carry>0:
            tail.next = ListNode(carry)
        return head