# Find Peak Element (LeetCode 162) - Binary Search
# Approach: Handle the edges first (index 0 or n-1 can be a peak, and a
#           1-element array is a peak). Then binary search on 1..n-2: if mid is
#           bigger than both neighbours it's a peak; otherwise walk uphill,
#           toward the bigger neighbour, because going uphill must reach a peak
#           (the ends count as -infinity). Any peak is accepted.
#           The commented-out version is the shorter standard one: compare
#           nums[mid] with nums[mid + 1] and keep the uphill half until
#           left == right.
# Time: O(log n)  |  Space: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Monotonic Binary search question
        # Either of the peak elements is allowed
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     mid = (left+right) //2 
        #     if nums[mid] > nums[mid+1]:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left

        left, right = 1, len(nums) - 2
        n = len(nums)
        #Edge conditions
        if n > 1 and nums[0] > nums[1]:
            return 0
        if n > 1 and nums[-1] > nums[-2]:
            return n - 1
        if n == 1:
            return 0
        
        while left <= right:
            mid = (left+right) // 2
            prev = (mid-1) % n 
            nxt = (mid+1) % n

            if nums[mid] > nums[prev] and nums[mid] > nums[nxt]:
                return mid
            elif nums[nxt] > nums[mid]:
                left = mid + 1
            elif nums[prev] > nums[mid]:
                right = mid - 1        
