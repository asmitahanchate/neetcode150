# Container With Most Water (LeetCode 11) - Two Pointers
# Approach: Start with the widest container (left = 0, right = n - 1).
#           Area = width * the shorter height. Then move the pointer at the
#           SHORTER line inward: moving the taller one can only shrink the
#           width while the shorter line still caps the height, so it can't help.
# Time: O(n)  |  Space: O(1)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        area = 0 
        maxArea = float("-inf")

        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            maxArea = max(maxArea,area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1 
        return maxArea
