# Two Sum (LeetCode 1)
# Approach: One pass with a hashmap of value -> index. For each number, check
#           whether its complement (target - num) was already seen; if so,
#           return both indices, otherwise record the current number.
# Time: O(n)  |  Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder ={}
        result = []
        # Keep building the hashmap as you go 
        for idx, num in enumerate(nums):
            if target - num in remainder:
                return [remainder[target-num],idx]
            remainder[num] = idx
        # Basically if you know it exists previously, just return it and 
        # Keep going till you find the second element
        # Time complexity - O(n) and space compleixty -O(n) for building 
        # The hashmap
