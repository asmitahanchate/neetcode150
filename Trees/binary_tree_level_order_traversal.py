# Binary Tree Level Order Traversal (LeetCode 102) - Trees, BFS
# Approach: BFS with a queue. At the start of each loop the queue holds
#           exactly one level, so take len(q) nodes (fixed before the for loop
#           starts), record their values in `level`, and add their children to
#           the back of the queue for the next round. Append `level` after the
#           whole level is processed.
# Time: O(n)  |  Space: O(n) (the queue holds up to one full level, ~n/2)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        #At every level when you do a level + 1 do a result.append(but after both the right and left nodes are processed)
        q = deque()
        if root:
            q.append(root)
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(level)
        return result
