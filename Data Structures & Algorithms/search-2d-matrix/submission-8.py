class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # i have to compare the top and bottom of the ends of cols
        top, bot = 0, len(matrix) - 1
        # we need to key in on a row that is lower or equal to target
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        if not top <= bot: # if the pointers are not equal to each other or they've gone past, there's no solution
            return False
        mid = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        return False