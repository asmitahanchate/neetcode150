# Maximum Sum Circular Subarray (LeetCode 918) - Kadane's algorithm
# Approach: Run Kadane's for both the max subarray and the min subarray in one
#           pass. A wrap-around subarray is everything except a middle chunk,
#           so its best sum is sum(nums) - minSum. Answer is the larger of
#           maxSum and sum(nums) - minSum, except when every number is
#           negative (maxSum <= 0): then minSum is the whole array, and the
#           answer is just maxSum.
# Time: O(n)  |  Space: O(1)

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # Instead of going into an actual circular array think of
        # Min subarray which automatically when subtracted from 
        # sum(nums) gives you the maxSubarray
        # The only edge case is when the entire array is negative
        # Then you just take the largest out of them and that's max sum
        maxSum,minSum = nums[0], nums[0]
        currMax, currMin = 0,0

        for num in nums:
            currMax = max (currMax+num, num)
            currMin = min(currMin+num, num)
            maxSum = max(maxSum,currMax)
            minSum = min(minSum,currMin)
        return max(maxSum, sum(nums)-minSum) if maxSum > 0 else maxSum
