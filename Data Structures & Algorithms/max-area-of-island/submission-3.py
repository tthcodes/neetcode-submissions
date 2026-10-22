class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # grid is lists of lists, with INT, not str.
        # we're gonna need to have a search for unvisited islands. but during that search we need to be all unvisited land as well as keeping a MAX. i think we can keep curr and max outside of that search.

        # these are our global vars 
        maxArea = 0
        currArea = 0 
        visited = set() 

        # define discover - our helper function for when we find new land
        def discover(land):
            nonlocal currArea
            nonlocal maxArea

            #grab coordinates 
            r, c = land 

            # we need to check if current coordinates are INBOUNDS of grid, if not return
            if (
            r < 0 or r > rows - 1 or c < 0 or c > cols - 1
            ):
                return 

            # check for if it's been discovered OR if it is water
            if land in visited or grid[r][c] == 0:
                return 

            else: # otherwise it's new land, so add it to visited, then update currArea/maxArea
                currArea += 1
                maxArea = max(maxArea, currArea)
                visited.add(land)

            # after updating or returning, recursively call.. when do we declare boundaries? before recursive call or after during function? i think during, then we can call
            discover((r - 1, c))
            discover((r + 1, c))
            discover((r, c + 1))
            discover((r, c - 1))

        # now we can iterate 
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                position = (r, c)
                # if current position is water OR already visited, move on.
                if position in visited or grid[r][c] == 0: 
                    continue
                # otherwise, initiate discover, RESET currArea to 0 after 
                else:
                    discover((r, c))
                    currArea = 0 

        # now we return maxArea
        return maxArea 

        # dry run
        # grid = [[1, 1], [0, 1]] -> 3 
