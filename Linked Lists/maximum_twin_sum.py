# Maximum Twin Sum of a Linked List (LeetCode 2130) - Linked List
# Approach (array, re-solved Nov 23): copy the values into a list, then two
#           pointers from both ends: twin pairs are (0, n-1), (1, n-2), ...
#           Track the largest pair sum.
# Time: O(n)  |  Space: O(n) for the list
# O(1)-space version (reverse the first half while finding the middle):
#           see maximum_twin_sum_revisiting.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        left, right = 0, len(result) -1
        maxRes = 0
        while left < right:
            maxRes = max(maxRes, result[left] +result[right])
            left += 1
            right -= 1
        return maxRes
