class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            if row[r] < target:
                continue
            else:
                while l <= r:
                    m = (l + r) // 2
                    if row[m] > target:
                        r = m - 1
                    elif row[m] < target:
                        l = m + 1
                    elif row[m] == target:
                        return True
                    else:
                        return False
        return False