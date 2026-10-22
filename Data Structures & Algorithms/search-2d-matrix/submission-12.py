class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row in non-decreasing order
        # same as first int in each row
        top, bot = 0, len(matrix) - 1
        mid = 0
        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                mid = m
                print('found', mid)
                break
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False