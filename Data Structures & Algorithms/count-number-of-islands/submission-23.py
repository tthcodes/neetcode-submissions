class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                # takeaway is that we need to ensure we're putting the right thing into the helper function.
        # and there's an order for guardrails 

        res = 0

        # init visited 
        visited = set()

        # helper func 
        def dfs(r, c): 
            # base case 
            if (r, c) in visited or c < 0 or c >= len(grid[0]) or r < 0 or r >= len(grid) or grid[r][c] == '0':
                return 
            
            # if it passes base case, then we add to visited 
            visited.add((r, c))

            # then recurse each direction 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1) 
            
        # then we iterate over the grid and perform dfs on each unique island

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                
                res += 1 

                dfs(r, c)

        return res 
