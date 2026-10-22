class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create graph
        grid = [[1] * m for _ in range(n)]

        # starting at bottom right, increase from bottom and right 
        for r in range(n - 2, -1, -1):
            for c in range(m - 2, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
        
        return grid[0][0]
