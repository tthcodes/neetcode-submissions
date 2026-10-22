class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(land):
            r, c = land
            if r > rows - 1 or r < 0 or c > cols - 1 or c < 0 or land in visited or grid[r][c] == 0:
                return 0
            
            else:
                visited.add(land)
                return (
                    1 +
                    dfs((r - 1, c)) +
                    dfs((r + 1, c)) +
                    dfs((r, c + 1)) +
                    dfs((r, c - 1))
                )
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs((r,c)))
        return maxArea