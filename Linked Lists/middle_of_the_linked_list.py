# Middle of the Linked List (LeetCode 876) - Linked List, fast & slow pointers
# Approach: slow moves 1 step, fast moves 2 steps. When fast reaches the end,
#           slow is at the middle. For an even length, fast stops at None and
#           slow lands on the SECOND middle node, which is what this problem asks for.
# Time: O(n)  |  Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
