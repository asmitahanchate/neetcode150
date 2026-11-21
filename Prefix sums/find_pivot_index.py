# Find Pivot Index (LeetCode 724) - Prefix sums
# Approach: prefix[i] = sum of nums[0..i], postfix[i] = sum of nums[i..end]
#           (built right to left, then reversed). Both include nums[i], so
#           prefix[i] == postfix[i] means left sum == right sum -> pivot.
#           The commented-out version is also correct and uses O(1) space:
#           running_sum (0..i) vs total (i..end), shrinking total as you go.
# Time: O(n)  |  Space: O(n) (O(1) for the commented-out version)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total = sum(nums)
        # running_sum = 0

        # for i in range(len(nums)):
        #     running_sum+= nums[i]
        #     if running_sum == total:
        #         return i
        #     total = total -nums[i]
        # return -1

        prefix = []
        postfix = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            postfix.append(total)
        postfix.reverse()
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1
