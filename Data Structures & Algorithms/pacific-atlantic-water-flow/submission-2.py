class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # input is a matrix of m x n. 

        # pacific touches top and left
        # atlantic touches bottom and right 

        # output is a list of grid positions that can flow to both
        # water only flows from cell to neighbor if neighbor's height is <= source

        # time and space complexity 
        '''
        time: we potentially visit the whole grid and for each one we evaluate if it belongs to pacific and/or atlantic, so O(M x N). 

        space: potentially can store the whole grid in both sets, so 2O(M x N) boils down to O(M x N) so no constants. the call stack can also go up to the whole grid. 
        '''

        # init pacific and atlantic set
        pac, atl = set(), set()

        # init res 
        res = []

        # init row and col length
        rows, cols = len(heights), len(heights[0])

        # need the helper function. and we pass forward the grid position, the ocean we're inquiring about, and the prevheight to compare 

        def dfs(r, c, ocean, prevHeight):

            # base case, we return if it's beyond the grid, if it's already in the ocean, or the currentheight is < the previous because we're starting from the edges, this position should be higher or equal to previous to flow out
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight or (r, c) in ocean:
                return 
            
            # otherwise we know it can flow out to that ocean, so add, then proceed to 4 quadrants 
            ocean.add((r, c)) 
            
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        # now we need to loop through the edges 
        for r in range(rows):
            # top, left edge = pac
            # bottom, right edge = atl 
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1]) 

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # now we iterate through one set and append matches
        for (r, c) in atl:
            if (r, c) in pac:
                res.append([r, c])

        return res 
            
