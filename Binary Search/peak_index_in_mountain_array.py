# Peak Index in a Mountain Array (LeetCode 852) - Binary Search
# Approach: Same as Find Peak Element, but there's exactly one peak. Compare
#           arr[mid] with arr[mid + 1]: going down -> the peak is at mid or to
#           its left (right = mid); going up -> the peak is to the right
#           (left = mid + 1). When left == right, that's the peak.
#           mid + 1 is always in bounds because mid < right inside the loop.
# Time: O(log n)  |  Space: O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # No edge cases like peak element because only 1 peak element
        # Constraints say min array length is 3 so no need to check for len
        left, right = 0, len(arr) -1 
        while left < right:
            mid = (left+right) // 2
            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left 
