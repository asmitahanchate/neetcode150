# 3Sum (LeetCode 15) - Two Pointers
# Approach: Sort. For each number a (skipping duplicates), run Two Sum II with left/right
#           pointers on the rest for -a; after a match, skip duplicate left values.
# Time: O(n^2)  |  Space: O(1) extra (besides sorting/output)
# Source: my original solution from revisiting_leetcode/3sum.py

# Pretty un-intuitive problem for a beginner. Do this again 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force approach is to have 3 loops 
        # How you would have in Two sum for 2 loops and comparison of each ele
        # Or apply a+b+c ==0 i.e., a+b = -(c)
        sorted_nums = sorted(nums)
        print(sorted_nums)
        result = []

        # Firstly you check if its NOT the first value and its not the same value 
        for idx, a in enumerate(sorted_nums):
            if idx > 0 and a == sorted_nums[idx - 1]: # This checks for the left neighbour
                continue 
            left, right = idx + 1, len(sorted_nums) - 1 # Will only look ahead from that index, hence left is idx + 1

            while left < right:
                if a + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1 
                elif a + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                else:
                    result.append([a, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    # Inner loop for going until two numbers are distinct
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left +=1
        return result
            

        
