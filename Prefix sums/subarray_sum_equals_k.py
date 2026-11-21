# Subarray Sum Equals K (LeetCode 560) - Prefix sums + hashmap
# TODO: COME BACK TO THIS AND SOLVE IT AGAIN.
#
# Approach: A subarray (i+1..j) sums to k when prefix[j] - prefix[i] == k,
#           i.e. prefix[i] == currSum - k. Keep a hashmap of how many times each
#           running sum has appeared; at each step add the count of currSum - k.
#           {0: 1} = the empty prefix (sum 0 seen once), so subarrays starting
#           at index 0 are counted. Same idea as Two Sum, on prefix sums.
# Why not a sliding window: nums can be negative (and zero), so "sum too big"
#           doesn't mean dropping the left side helps, and a window can't count
#           several subarrays ending at the same index.
# Time: O(n)  |  Space: O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSums ={0:1} #Base case of 0 i.e., nothing that has a prefix sum of 1 
        for n in nums:
            currSum += n
            diff = currSum - k  
            res += prefixSums.get(diff,0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum,0)
        return res
