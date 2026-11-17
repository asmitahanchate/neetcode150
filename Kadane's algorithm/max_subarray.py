# Maximum Subarray (LeetCode 53) - Kadane's algorithm
# Approach: Walk the array keeping the best sum of a subarray ending here
#           (currSum). At each number, either extend the previous subarray or
#           start fresh at this number, whichever is larger; track the best
#           currSum seen as maxSum. maxSum starts at -inf so an all-negative
#           array still returns its largest element.
# Time: O(n)  |  Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0

        for num in nums:
            currSum += num
            currSum = max(currSum,num)
            maxSum = max(maxSum,currSum)
        return maxSum 
        
        #Kadane's algorithm set it to 0 but you can't set it to 0
        # If all numbers are negative so compare currSum to num directly 
