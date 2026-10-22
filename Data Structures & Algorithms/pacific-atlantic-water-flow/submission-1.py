class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set() 
        res = []

        def dfs(r, c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in ocean or prevHeight > heights[r][c]:
                return 
            
            ocean.add((r, c))

            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        # atlantic = bottom and right
        # pacific = top and left 
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        for (r, c) in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        
        return res
