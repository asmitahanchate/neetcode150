# Maximum Twin Sum of a Linked List (LeetCode 2130) - Linked List
# Source: my original solution from revisiting_leetcode/maximum_twin_sum_of_a_linked_list.py
#
# This file has two versions. Both classes are named Solution, so the SECOND
# one (the O(1)-space version) is the one that runs.
#   1. Array: copy values into a list, pair res[left] + res[right]. O(n) time, O(n) space.
#   2. Reverse while finding the middle: fast moves 2 steps while slow moves 1
#      and reverses the links behind it. When fast reaches the end, prev is the
#      reversed FIRST half and slow is the start of the second half; walk both
#      together, so each step pairs a node with its twin. O(n) time, O(1) space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        left = 0
        right = len(res) - 1
        currSum = 0
        maxSum = 0

        for i in range(len(res)):
            currSum = res[left] + res[right]
            maxSum = max(maxSum, currSum)
            left +=1 
            right -=1

        return maxSum
    # Time complexity - O(n) traversing both the linked list and the new array
    # Space complexity - O(n) for the new array

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Rversing a linked list
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev 
            prev = slow
            slow = temp 

        result = 0
        while slow:
            result = max(result, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return result

        # Time complexity - O(n)
        # Space complexity - O(1)
