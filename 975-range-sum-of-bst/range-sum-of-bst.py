# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        def RangeSum(node, low , high):
            if node is None:
                return 0
            
            if node.val < low:
                return RangeSum(node.right, low , high)
            if node.val > high:
                return RangeSum(node.left, low , high)
            
            return ( node.val + RangeSum(node.left, low, high) + RangeSum(node.right, low , high))
        return RangeSum(root, low, high)