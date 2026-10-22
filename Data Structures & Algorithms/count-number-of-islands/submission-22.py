class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we'll need a visited set to keep track of islands 
        visited = set()

        # we'll use DFS to explore each unique island, we'll need to guard exploration between row and col limits
        def dfs(r, c):
            # base case is if it's water or in visited, we return.. ALSO if it's beyond row/col count
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == '0' or (r, c) in visited:
                return 
            
            # otherwise we add to visited as we expore, and invoke to 4 quadrants 
            visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # init counter
        res = 0

        # iterate through every col/row once total, pool dfs draws from doesn't replenish on its call 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if the position isn't '0' and is not in 'visited', we increment res, and invoke dfs
                if grid[r][c] == '0' or (r, c) in visited:
                    continue
                
                # since it's not either 0 or visited, we increment res, and invoke dfs, we'll leave adding to visited within DFS, since this will be needed for each discovery
                res += 1 
                dfs(r, c)

        # return res once all r/c has been discovered and islands explored
        return res  
