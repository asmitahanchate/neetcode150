# Contains Duplicate II (LeetCode 219) - Sliding window (fixed size)
# Approach: Keep a set holding at most the last k numbers (the window).
#           Before checking nums[right], drop nums[left] once the window would
#           span more than k indices. If nums[right] is already in the set,
#           two equal values are within k of each other.
# Time: O(n)  |  Space: O(min(n, k))

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() #declare an empty window 
        left = 0 # left starts at 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False
