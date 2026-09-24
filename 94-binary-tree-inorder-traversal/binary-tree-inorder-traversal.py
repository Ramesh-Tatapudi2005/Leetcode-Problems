# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, node,ans):
        if node is None:
            return ans
        ans = self.inorder(node.left, ans)
        ans.append(node.val)
        ans = self.inorder(node.right, ans)
        return ans 
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        ans = []
        ans = self.inorder(root, ans)
        return ans