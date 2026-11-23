# Linked List Cycle (LeetCode 141) - Linked List, Floyd's fast & slow pointers
# Approach: slow moves 1 step, fast moves 2. If there's no cycle, fast reaches
#           the end (None). If there is a cycle, fast laps around and must
#           eventually land on the same node as slow (it gains 1 step per loop).
# Time: O(n)  |  Space: O(1)  (a visited set also works, but costs O(n) space)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
