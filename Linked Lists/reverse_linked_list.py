# Reverse Linked List (LeetCode 206) - Linked List
# Approach: Walk the list once with prev and curr. Save curr.next in temp,
#           point curr.next back to prev, then move prev and curr one step
#           forward. When curr is None, prev is the new head.
# Time: O(n)  |  Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        if not head:
            return None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev #New beginning of the list

        # Time complexity - O(n)
        # Space complexity - O(1)
