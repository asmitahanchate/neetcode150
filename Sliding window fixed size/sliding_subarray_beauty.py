# Sliding Subarray Beauty (LeetCode 2653) - Sliding window (fixed size)
# TODO: COME BACK TO THIS AND SOLVE IT AGAIN.
#       This version is correct but times out (708/717 tests pass).
#
# Approach (this version): keep the window in a list, sort it each step,
#           read the x-th smallest; if it isn't negative, the beauty is 0.
# Time: O(n * k log k)  |  Space: O(k)  -> too slow for large n and k
#
# To redo: values are only -50..50, so keep a tally (count) of each value in
#          the window instead of sorting. To find the x-th smallest, count up
#          from -50 to -1 until you've seen x numbers. O(50 * n) = O(n) time.

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        currList = []
        result = []

        left = 0
        for right in range(len(nums)):
            currList.append(nums[right])
            currList.sort() #Too slow O(nlogn) so time limit exceeds. 708/717 pass
            if (right-left + 1) == k:
                if currList[x-1] < 0:
                    result.append(currList[x-1])
                else:
                    result.append(0)
                currList.remove(nums[left])
                left += 1
        return result
