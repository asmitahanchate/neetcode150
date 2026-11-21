# Product of Array Except Self (LeetCode 238) - Prefix sums (products)
# Approach: prefix[i] = product of everything LEFT of i (starts at 1),
#           postfix[i] = product of everything RIGHT of i (built right to left,
#           then reversed). answer[i] = prefix[i] * postfix[i]. No division.
# Time: O(n)  |  Space: O(n) for the prefix and postfix lists
#       (O(1) extra if you write prefix into the result and multiply postfix in
#        on a second pass, like Arrays and Hashing/product_of_array_except_self.py)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Product of self postfix and prefix sums concept
        prefix = []
        pre = 1
        for i in range(1,len(nums)+1):
            prefix.append(pre)
            pre *= nums[i-1]
        postfix = []
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(post)
            post *= nums[i]
        result = []
        postfix = postfix[::-1]
        for i, j in zip(prefix,postfix):
            result.append(i*j)
        return result
        # Time complexity - O(n)
