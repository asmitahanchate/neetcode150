# Minimum Size Subarray Sum (LeetCode 209) - Sliding window (variable size)
# Approach: Grow the window by moving right and adding nums[right] to total.
#           While total >= target, the window is valid: record its length,
#           then shrink it from the left to look for a shorter valid window.
#           Each index enters and leaves the window at most once.
# Time: O(n)  |  Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        left, total = 0, 0
        # Remember right always goes till the end
        # Its just the left pointer or inner loop
        # That may or may not go till right
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                #Keep shringking the window 
                length = min(right - left + 1, length)
                # Keep removing left from total
                total -= nums[left]
                # Keep incrementing left
                left += 1
        return 0 if length == float("inf") else length 
