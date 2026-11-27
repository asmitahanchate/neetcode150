# Balanced Binary Tree (LeetCode 110) - Trees
# Approach: One bottom-up DFS that returns two things for every node:
#           [is this subtree balanced?, its height]. A node is balanced when
#           both children are balanced AND their heights differ by at most 1.
#           Height = 1 + the taller child. An empty node is [True, 0].
#           Computing height and balance together avoids recomputing heights
#           at every node (which would be O(n^2)).
# Time: O(n)  |  Space: O(h) for the recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]
            
        return dfs(root)[0]
