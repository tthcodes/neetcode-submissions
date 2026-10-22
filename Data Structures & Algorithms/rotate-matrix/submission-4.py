class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # return none
        # must rotate matrix in place. 
        # each matrix is a square, so col and row length same
        # n is between 1 and 20, nums can be +/- 1000
        # from the primitives, what we can do to flip this 90 degrees, is by transposing, switching row and column positions, THEN reversing row by row. 
        # but how do we keep track of two spots at the same time in order to flip them, without re-creating the matrix first? maybe we can implement another 'VISITED' so that we dont re-transpose.         rowsLen = len(matrix)
        n = len(matrix)
        # now we iterate over the matrix again to reverse each row
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in matrix:
            r.reverse()
