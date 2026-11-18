# Best Time to Buy and Sell Stock (LeetCode 121) - Sliding window (variable size)
# Approach: left is the buy day, right is the sell day. If prices[right] is
#           higher than prices[left], record the profit. Otherwise prices[right]
#           is a new lowest price, so jump left straight to right: no earlier
#           day can be a better buy for any later sell day.
# Time: O(n)  |  Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Basically sliding window approcach. Just that instead of incrementing left one by one just move it to right pointer if its not smaller than right 
        maxProfit, left = 0,0
        currProfit = 0
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                maxProfit = max (maxProfit,currProfit)
            else:
                left = right
        return maxProfit
