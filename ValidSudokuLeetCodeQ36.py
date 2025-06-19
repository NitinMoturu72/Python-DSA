# Valid Sudoku

# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        start = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]

        for i, j in start:
            s = set()
            for row in range(i, i+3):
                for column in range(j, j+3):
                    item = board[row][column]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True

# Brute force approach:
# Row Check: For each row, we check if there are any duplicates of numbers 1-9 using a set. Return False if a duplicate is found. Else if the item is not a '.', we add it to the set.
# Column Check: For each column, we do the same check for duplicates.
# Box Check: For each of the nine 3x3 boxes, we check for duplicates in the same way as above.
# Time Complexity: O(n^2), where n is the number of cells in the board (81 for a 9x9 board).
# Space Complexity: O(1), since we are using a constant amount of extra space for the sets.


def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in box[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])
        return True

# Hash sets approach:
# We use three hash sets to keep track of the numbers seen in each row, column, and 3x3 box.
# For each cell in the board, we check if the number is already in the corresponding row, column, or box set.
# If it is, we return False. Otherwise, we add the number to the respective sets
# If theboard passes all checks, we return True.
# Time Complexity: O(n^2), where n is the number of cells in the board (81 for a 9x9 board).
# Space Complexity: O(1), since we are using a constant amount of extra space for the sets, which is bounded by the number of unique numbers (1-9).