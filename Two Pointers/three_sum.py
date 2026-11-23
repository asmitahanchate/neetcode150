# 3Sum (LeetCode 15) - Two Pointers  (re-solved Nov 23)
# Approach: Sort. For each i (skip it if nums[i] == nums[i - 1], so the same
#           first number isn't used twice), run Two Sum II on the rest with
#           left = i + 1 and right = end: sum < 0 -> left += 1, sum > 0 ->
#           right -= 1. On a match, record it, move left/right past their
#           duplicates, then step both once more.
#           Bug fixed on the way: the final left += 1 / right -= 1 must be
#           inside the else (only after a match), or both pointers jump on
#           every comparison and skip valid triples.
# Time: O(n^2)  |  Space: O(1) extra (besides sorting and the output)
# (Older solution from revisiting_leetcode: three_sum_revisiting.py)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
