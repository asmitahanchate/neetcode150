# Binary Tree Inorder Traversal (LeetCode 94) - Trees
# Approach: Recursive DFS with an inner helper: visit left subtree, then the
#           node itself, then the right subtree (Left -> Node -> Right).
#           The helper appends to one shared result list, so nothing needs to
#           be returned from each call. Inner helpers are called without self.
#           For a BST, inorder gives the values in sorted order.
# Time: O(n)  |  Space: O(h) for the recursion stack (+ O(n) for the output)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        node = root
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result 
