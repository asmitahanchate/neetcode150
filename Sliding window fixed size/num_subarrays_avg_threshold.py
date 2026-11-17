# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# (LeetCode 1343) - Sliding window (fixed size)
#
# Approach:
#   Every window has exactly k elements, so instead of re-summing each window
#   (O(n * k)), keep a running sum and slide it one step at a time:
#
#     1. Pre-load the first k - 1 elements into currSum.
#     2. For each window start `left` (there are len(arr) - k + 1 windows):
#          - add the element entering on the right:  arr[left + k - 1]
#            -> currSum is now the sum of exactly k elements
#          - if currSum / k >= threshold, count this window
#          - subtract the element leaving on the left: arr[left]
#            -> currSum is back to k - 1 elements, ready for the next window
#
#   Example: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
#     windows: [2,2,2] [2,2,2] [2,2,5] [2,5,5] [5,5,5] [5,5,8]
#     averages:  2       2       3      4       5       6      -> answer 3
#
#   Tip: currSum >= k * threshold avoids division and works the same.
#
# Time: O(n)  |  Space: O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        currSum = sum(arr[:k-1])
        for left in range(len(arr) - k+1):
            #We did this because we don't want to go till the end 
            currSum += arr[left + k - 1] #entire window size 
            if (currSum/k) >= threshold:
                result += 1 
            currSum -= arr[left] #Subtract the left one from sum
        return result
