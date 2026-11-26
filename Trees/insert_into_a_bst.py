# Insert into a Binary Search Tree (LeetCode 701) - Trees
# Approach: Recursion. An empty spot is where the new value goes, so return a
#           new TreeNode there. Otherwise go right if val is bigger, left if
#           smaller, and re-attach whatever the recursive call returns
#           (root.right = ... / root.left = ...). Return root so the parent
#           keeps its subtree.
# Time: O(h), h = tree height (O(log n) balanced, O(n) worst case)
# Space: O(h) for the recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right,val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        return root
