# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head or not head.next:
        #     return False
        # # visited = set()
        # # curr = head
        # # while curr :
        # #     if curr in visited:
        # #         return True
        # #     visited.add(curr)
        # #     curr = curr.next
        # # return False

        #Floyd's Twooo pointers slow pointer and fast pointer
        # It finds that the slow and fast pointer are equal if they then the cycle is found

        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False