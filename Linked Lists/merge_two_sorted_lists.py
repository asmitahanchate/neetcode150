# Merge Two Sorted Lists (LeetCode 21) - Linked List
# Approach: A dummy node gives the merged list a fixed starting point. While
#           both lists have nodes, attach the smaller one to node.next and
#           advance that list; then move node forward. When one list runs out,
#           attach the rest of the other (node.next = list1 or list2).
#           Return dummy.next, the real head.
# Time: O(m + n)  |  Space: O(1) (reuses the existing nodes)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = node = ListNode()

        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1

        # while list1 and list2:
        #     if list1.val <list2.val:
        #         node.next = list1
        #         list1 = list1.next
        #     else:
        #         node.next = list2
        #         list2 = list2.next
        #     node = node.next

        # node.next = list1 or list2
        # return dummy.next

        # # Time complexity - O(m+n)
        # # Space complexity - O(1)

        dummy = node = ListNode() # Basically like an empty list just LL form
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
