# Find the Duplicate Number (LeetCode 287) - Linked List / Floyd's cycle detection
# Approach: n + 1 numbers, each in 1..n, so treat each value as a "next"
#           pointer (i -> nums[i]). Starting at index 0, this walk must enter a
#           cycle, and the cycle's entrance is the duplicate (two indexes point
#           to it). Phase 1: slow moves 1 step, fast moves 2, until they meet.
#           Phase 2: start slow2 at 0; move slow and slow2 one step at a time;
#           where they meet is the cycle entrance = the duplicate.
# Time: O(n)  |  Space: O(1), and nums isn't modified

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(1) space so can't have a Counter 
        # The challenge is to not modify nums
        # How do we not have a set 
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return n 
        #     seen.add(n)
        # Using fast and slow pointers
        # The constraints are that len = n + 1 while numbers are till n
        # So basically think of postions as pointers 
        # 1->3->4->2->2
        #Also worse complexity so don't even try
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
