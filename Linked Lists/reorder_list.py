# Reorder List (LeetCode 143) - Linked List
# Source: my original solution from revisiting_leetcode/reorder_linked_list.py
#
# This file has two classes named Solution, so only the SECOND one runs.
#   1. List + two pointers (first class): copies values and builds the new
#      order in `result`, but only prints it; it never changes the linked list,
#      and it drops the middle value when the length is odd. Kept as my first try.
#   2. In place (second class, the real answer): find the middle with
#      slow/fast pointers, cut the list there, reverse the second half, then
#      merge the two halves alternately (first, last, second, second-last, ...).
# Time: O(n)  |  Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Simplest is to make a list and then do a two pointer 
        linkedlist= []
        curr = head
        while curr:
            linkedlist.append(curr.val)
            curr = curr.next
        left = 0
        right = len(linkedlist) - 1

        result = []
        while left < right:
            result.append(linkedlist[left])
            result.append(linkedlist[right])
            left += 1
            right -= 1
        print(result)
    # Time complexity - O(n) to go through list and then go through the array
    # Space complexity - O(2n) to save linkedlist and result arrays

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head 
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None 
        while second:  #This part is exactly reversal 
            temp = second.next  # Have a temp ahead of curr
            second.next = prev  # Point curr.next to prev
            prev = second # prev comes ahead to curr
            second = temp  # curr goes ahead to temp
        
        # List after this reversal 
        # 0->1->2->3->6->5->4
        # first is 0 and second is 6
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            # tmp1 = 1 and tmp2 = 5
            first.next = second # Point 0 to 6 after reversal
            second.next = tmp1 # Point 6 to 1
            first,second = tmp1, tmp2 # Move both ahead 


