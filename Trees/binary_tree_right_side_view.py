# Binary Tree Right Side View (LeetCode 199) - Trees, BFS
# Approach: Level-order BFS. Before processing a level, the queue holds exactly
#           that level from left to right, so q[-1] is its rightmost node:
#           record it, then pop the whole level and add the children.
# Time: O(n)  |  Space: O(n) (the queue holds up to one full level)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []
        q = deque()

        if root:
            q.append(root)
        while len(q) > 0:
            result.append(q[-1].val)
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return result
