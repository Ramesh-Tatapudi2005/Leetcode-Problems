# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def FindSum(self, node, targetSum, sum):
        if node is None:
            return 
        
        if node.left is None and node.right is None:
            sum += node.val
            if sum == targetSum:
                return True

        left = self.FindSum(node.left, targetSum, sum+node.val)
        right = self.FindSum(node.right, targetSum, sum + node.val)

        if left or right:
            return True
        return False
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        return self.FindSum(root, targetSum,0)