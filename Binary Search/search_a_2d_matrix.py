# Search a 2D Matrix (LeetCode 74) - Binary Search
# TODO: COME BACK TO THIS PROBLEM.
#
# Approach: Two binary searches.
#   1. Binary search the ROWS: if target > the row's last value, go down;
#      if target < the row's first value, go up; otherwise the target can only
#      be in this row. If top passes bottom, no row fits -> False.
#   2. Binary search the COLUMNS inside that row like a normal sorted list.
#   (Alternative: treat the matrix as one sorted list of m * n numbers and
#    map an index i to matrix[i // cols][i % cols].)
# Time: O(log m + log n) = O(log(m * n))  |  Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Always use double binary search
        # First find the row to work on
        # In that row have left and right pointers
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        # Did not find any row 
        if not (top <= bottom):
            return False
        row_to_work_on = (top + bottom) // 2
        left, right = 0,cols-1
        while left <= right:
            mid = (left+right) // 2
            if target > matrix[row_to_work_on][mid]:
                left = mid + 1
            elif target < matrix[row_to_work_on][mid]:
                right = mid - 1
            else:
                return True
        return False

        # Time complexity - O(logm + logn)
        # Space complexity - O(1)
