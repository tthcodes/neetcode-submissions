class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return false if it's not valid, true if valid
        # we need to create 3 entities for each category: row, col, box. i think dict and the vals are lists
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        # we're going to iterate over the board and add to each row, col, and box, at their respective sections.
        # input is strings, not ints 
        # if it is a '.', we skip 
        for r in range(len(board)):
            for c in range(len(board)): # since box is 9x9. 
                if board[r][c] == '.':
                    continue 
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[tuple([r//3, c//3])]:
                    return False
                else:
                    cur = board[r][c]
                    rows[r].add(cur)
                    cols[c].add(cur)
                    boxes[tuple([r//3, c//3])].add(cur)
        # then once we're done we return True
        return True 

            #quick dry run
            # board = [[1, 2]] -> True, gets added to index 0 (both do), but separate columns for 1, 2, same boxes for 1,2 .. but all unique so it returns True. Do not want to do a bigger sample for a longer dry run. 
