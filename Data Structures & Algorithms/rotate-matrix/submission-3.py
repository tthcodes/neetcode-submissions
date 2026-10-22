class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # return none
        # must rotate matrix in place. 
        # each matrix is a square, so col and row length same
        # n is between 1 and 20, nums can be +/- 1000
        # from the primitives, what we can do to flip this 90 degrees, is by transposing, switching row and column positions, THEN reversing row by row. 
        # but how do we keep track of two spots at the same time in order to flip them, without re-creating the matrix first? maybe we can implement another 'VISITED' so that we dont re-transpose. 
        visited = set() # insert the transposed position into here so it can skip.
        rowsLen = len(matrix)
        colsLen = len(matrix[0])
        for r in range(rowsLen):
            for c in range(colsLen):
                if (r, c) in visited:
                    continue
                temp = matrix[c][r]
                matrix[c][r] = matrix[r][c]
                matrix[r][c] = temp
                visited.add((c, r))
        # now we iterate over the matrix again to reverse each row
        for r in range(rowsLen):
            matrix[r] = matrix[r][::-1]
