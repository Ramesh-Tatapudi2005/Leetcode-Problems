# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def FindSum(self, node, isLeft):
        if node is None:
            return 0
        if isLeft and node.left is None and node.right is None:
            return node.val
        return self.FindSum(node.left, True) + self.FindSum(node.right, False)
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        return self.FindSum(root, False)