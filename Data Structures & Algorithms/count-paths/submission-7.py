class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # initiate beginning row that represents current bottom row
        # since each element at row 1 only has one possibility, and we count the actual end spot as 1. 
        currRow = [1] * n
        for _ in range(m - 1):
            # initialize the new row that is on top of curr
            newRow = [1] * n
            # now we loop again to start from the END column, but we skip the last column since we know it'll be all 1 AND only 1 is possible cause it can only go down.
            for i in range(n - 2, -1, -1):
                newRow[i] = newRow[i + 1] + currRow[i] # this adds all steps to the right possible + all steps below possible. 
            # now we want to replace currRow with newRow until we have the first row
            currRow = newRow
        return currRow[0]
