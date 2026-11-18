# Two Sum II - Input Array Is Sorted (LeetCode 167) - Two Pointers
# Approach: Start left at the smallest and right at the largest number.
#           If the sum is too big, move right down (smaller number); if too
#           small, move left up (bigger number). The sorted order guarantees
#           we never skip the answer. Return 1-indexed positions.
# Time: O(n)  |  Space: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1 ]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
