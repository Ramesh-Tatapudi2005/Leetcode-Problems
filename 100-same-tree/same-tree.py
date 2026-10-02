# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Checksame(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.Checksame(p.left, q.left) and self.Checksame(p.right, q.right)
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        return self.Checksame(p,q)