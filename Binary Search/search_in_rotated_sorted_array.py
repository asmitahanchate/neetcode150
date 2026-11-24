# Search in Rotated Sorted Array (LeetCode 33) - Binary Search
# Approach: One pass. At each mid, one half is always sorted:
#           - nums[mid] >= nums[start] -> left half (start..mid) is sorted.
#             If target is outside it (target > nums[mid] or target < nums[start]),
#             go right; otherwise go left.
#           - else the right half (mid..end) is sorted.
#             If target is outside it (target < nums[mid] or target > nums[end]),
#             go left; otherwise go right.
#           Use >= so a 1-element left half (start == mid) counts as sorted.
# Time: O(log n)  |  Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = (start+end) // 2
            if target == nums[mid]:
                return mid

            #left sorted portion of the array
            if nums[mid] >= nums[start]:
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            #right sorted portion of the array
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1
