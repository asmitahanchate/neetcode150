# Find Minimum in Rotated Sorted Array (LeetCode 153) - Binary Search
# Approach: The minimum is the only element smaller than both neighbours
#           (with % n wrap-around). Otherwise move toward the side where the
#           numbers go DOWN: nums[left] > nums[mid] -> drop is on the left;
#           nums[right] < nums[mid] -> drop is on the right. If neither, the
#           window only goes up, so the minimum is at its start -> go left.
#           That last else branch is what stopped the infinite loop (TLE).
#           return nums[0] after the loop covers a 1-element array.
# Time: O(log n)  |  Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start = 0
        # end = len(nums) -1

        # if len(nums) == 1:
        #     return nums[0]
        
        # #Array is not rotated
        # if nums[end]> nums[0]:
        #     return nums[0]

        # while start < end:
        #     mid = (start+end) //2
        #     if nums[mid]> nums[mid+1]:
        #         return nums[mid+1]

        #     if nums[mid-1]>nums[mid]:
        #         return nums[mid]
            
        #     if nums[mid] > nums[start]:
        #         start = mid +1
        #     else:
        #         end = mid -1 


        left, right = 0, len(nums) - 1
        n = len(nums)
        while left <= right:
            mid = (left+right) // 2
            prev = (mid-1) % n
            nxt = (mid+1) % n
            if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
                #Found min
                return nums[mid]
            # If not found min go towards unsorted portion
            elif nums[left] > nums[mid]:
                right = mid - 1
            elif nums[right] < nums[mid]:
                left = mid + 1
            # If no portion unsorted and everything is sorted 
            else:
                right = mid - 1 
        return nums[0] # If array is just 1 element
