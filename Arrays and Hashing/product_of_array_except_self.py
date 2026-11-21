# Product of Array Except Self (LeetCode 238) - Arrays & Hashing
# Approach: No division. First pass stores the product of everything to the left (prefix);
#           second pass, right to left, multiplies in the product of everything to the right.
# Time: O(n)  |  Space: O(1) extra (output array not counted)
# Source: my original solution from revisiting_leetcode/produc_of_array_except_self.py

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We have to solve it without division.
        # If division were allowed then it would have been simple because you take the entire product
        # Then keep dividing by each number in the array
        # Neetcode solution is to count the pre fix and post fix arrays that is in O(n)
        result = [1] * len(nums)
        # nums = [1,2,4,6]
        # result = [1,1,1,1]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            result[i] *=postfix
            postfix *= nums[i]
        return result
# Time complexity - O(n) we are gping through the nums array only once
# Space complexity - O(1) because the result array does not count but in general O(n) because of n elements being saved 
