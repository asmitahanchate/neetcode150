# Find in Mountain Array (LeetCode 1095, Hard) - Binary Search
# TODO: COME BACK TO THIS AND SOLVE / UNDERSTAND IT AGAIN.
#
# Approach: Three binary searches.
#   1. Find the peak (same loop as Peak Index in a Mountain Array):
#      get(mid) > get(mid + 1) -> going down, right = mid; else left = mid + 1.
#      Use while left < right (with <=, right = mid loops forever).
#   2. Search the uphill half 0..peak (ascending). Check it FIRST: a value can
#      appear on both sides, and the problem wants the smallest index.
#   3. If not found, search the downhill half peak+1..n-1 (descending).
#   One binary_search handles both halves with the ascending flag:
#   (val > target) == ascending -> go left, else go right.
#   Only .get(i) and .length() are allowed (no [] or len()); at most 100 calls.
# Time: O(log n)  |  Space: O(1)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        def binary_search(mountainArr, left, right, target,ascending):
            while left <= right:
                mid = (left+right) // 2
                val = mountainArr.get(mid)                                 
                if val  == target:
                    return mid
                elif (val > target) == ascending:
                    right = mid - 1
                else:
                    left = mid + 1 
            return -1        
        

        # Give the min or both function calls 
        # Peak element divides the array
        left, right = 0, mountainArr.length() - 1
        n = mountainArr.length()
        peak = 0
        while left < right:
            mid = (left+right) // 2
            if mountainArr.get(mid) > mountainArr.get(mid+1):
                right = mid
            else:
                left = mid + 1
        peak = left

        found = binary_search(mountainArr,0,peak,target,True)
        if found != -1:                                                 
            return found
        return binary_search(mountainArr,peak+1,n-1,target,False)
