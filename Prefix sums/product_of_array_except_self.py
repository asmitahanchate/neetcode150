# Product of Array Except Self (LeetCode 238) - Prefix sums (products)
# Approach: prefix[i] = product of everything LEFT of i (starts at 1),
#           postfix[i] = product of everything RIGHT of i (built right to left,
#           then reversed). answer[i] = prefix[i] * postfix[i]. No division.
# Time: O(n)  |  Space: O(n) for the prefix and postfix lists
#
# Optimized version (class SolutionOptimized, at the bottom): write the prefix
#           products straight into result, then walk right to left multiplying
#           in the postfix product. No extra lists.
# Time: O(n)  |  Space: O(1) extra (the result array doesn't count)

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


class SolutionOptimized:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        #To simplify this and do this all at once and not use extra memeory
        result = [1] * (len(nums)) #Intialize it all with 1s
        pre = 1

        # Start computing prefix
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            #Go in reverse and directly multiply
            result[i] *= post
            post *= nums[i]
        return result
