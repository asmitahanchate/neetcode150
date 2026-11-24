# Find First and Last Position of Element in Sorted Array (LeetCode 34) - Binary Search
# Approach: Two binary searches. On a match, the first pass keeps going LEFT
#           (right = mid - 1) to find the first occurrence; the second pass keeps
#           going RIGHT (left = mid + 1) to find the last. One pass can't do both,
#           because one pair of pointers can only move one way on a match.
#           If first is still inf, the target isn't there -> [-1, -1]
#           (index 0 is a valid answer, so don't check first > 0).
# Time: O(log n)  |  Space: O(1)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        idx = -1
        first, last = float("inf"), float("-inf")

        # First pass to find the first occurence
        while left <= right:
            mid = (right+left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                first = min(mid,first)
                right = mid - 1
            
        # Second pass to get the last occurence
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right+left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                last = max(mid,first)
                left = mid + 1
            
        
        return [first,last] if first != float("inf") else [-1,-1]
