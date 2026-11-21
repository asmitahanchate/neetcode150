# Valid Sudoku (LeetCode 36) - Arrays & Hashing
# Approach: One set per row, per column and per 3x3 box (key = (r//3, c//3)); a digit
#           already in any of its three sets means the board is invalid.
# Time: O(81) = O(1) for a fixed 9x9 board  |  Space: O(81) = O(1)
# Source: my original solution from revisiting_leetcode/valid_sudoku.py

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict (set)
        grid = defaultdict(set) # The key for this is r//3 and c//3
        # Basically checking duplicates in row and column is easy
        # But for the grid, what he did was each small value
        # Such has (4,4) or anything maps to a bigger grid value like (1,1)
        # Check the row first, then column, then square. Since 9*9 board 
        for r in range(9):   #Since its a double for loop its O(n^2)
            for c in range(9):
                if board[r][c] == ".":
                    continue # Do nothing if its a .
                if (board[r][c] in rows[r] # Check if the value we see is already a part of rows set
                or board[r][c] in columns[c]
                or board[r][c] in grid[(r//3, c//3)]):
                    return False

                columns[c].add(board[r][c]) # Syntax to add in a set
                rows[r]. add(board[r][c])
                grid[(r//3,c//3)].add(board[r][c])
        return True

# Time complexity - O(n^2)
# Space complexity - O(n^2)


