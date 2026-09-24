# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, ans):
        if node is None:
            return ans
        ans.append(node.val)
        ans = self.preorder(node.left, ans)
        ans = self.preorder(node.right, ans)
        return ans
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        return self.preorder(root, [])