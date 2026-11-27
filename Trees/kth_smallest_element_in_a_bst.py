# Kth Smallest Element in a BST (LeetCode 230) - Trees
# Approach: Inorder traversal (Left -> Node -> Right) of a BST visits the
#           values in sorted order, so collect them into a list and return
#           result[k - 1] (k is 1-indexed).
#           Follow-up: stop as soon as k values have been visited (count down
#           k in the dfs, or use an iterative stack) to avoid storing all n.
# Time: O(n)  |  Space: O(n) for the list (+ O(h) recursion stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        # For inorder traverse it inOrder and make a list 
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result[k-1]
