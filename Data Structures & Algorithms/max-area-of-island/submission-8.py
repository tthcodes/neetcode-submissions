class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        init max

        visited set init 

        helper dfs function
            returns if it's 0, or in visited set, or out of bounds 
            if it's 1, return + 1 somehow (forgot)
        
        loop over grid, init dfs when new island, set max if 

        '''
        res = 0

        rows, cols = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            down = dfs(r + 1, c)
            up = dfs(r - 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return down + up + left + right + 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited:
                    islandArea = dfs(r, c)
                    res = max(res, islandArea)

        
        return res 