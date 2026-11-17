# Contains Duplicate (LeetCode 217)
# Approach: A set keeps only unique values, so if converting nums to a set
#           shrinks its length, at least one value appeared more than once.
# Time: O(n)  |  Space: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
