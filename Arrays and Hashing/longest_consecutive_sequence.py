# Longest Consecutive Sequence (LeetCode 128) - Arrays & Hashing
# Approach (runs): sort the unique numbers and count runs of +1 -> O(n log n).
#           The set version below it (start only where num - 1 isn't in the set) is O(n),
#           but the first return means only the sorted version runs.
# Time: O(n log n) as written (O(n) for the set version)  |  Space: O(n)
# Source: my original solution from revisiting_leetcode/longest_consequitive_sequence.py

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Two pointer or maybe sliding window solution
        nums = sorted(set(nums))
        if len(nums) == 1:
            return 1
        left = 0
        curr = 1
        maxlen = 0

        for right in range(1, len(nums)):
            if nums[right] == nums[right-1] +1:
                curr += 1
            else:
                curr = 1
                left = right
            maxlen = max(maxlen, curr)
        return maxlen
        # Time complexity - O(NlogN) because of the sorting. Can we avoid that
        
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                longest = max(longest,length)
        return longest
        # Time complexity - O(n) instead of sorting we just keep checking the set

