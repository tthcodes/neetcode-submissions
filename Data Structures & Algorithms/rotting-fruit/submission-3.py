from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we're gonna wanna use deque, which allows us to pop left 
        # we only add to deque when it's an originally rotten orange
        # establish a fresh count 
        fresh = 0

        # establish time
        time = 0

        # establish a bound for row and col 
        rows = len(grid)
        cols = len(grid[0])

        # establish a direction array 
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # establish queue 
        queue = deque() 

        # now iterate over grid, add up fresh and append rotten coordinates to queue
        for r in range(rows):
            for c in range(cols):
                # now we want to continue 
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1 
        
        # now that we have the fresh count and queue we can do a while loop while either exist
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                # now we iterate through the directions, but we have to make a boundary before we move it
                for dr, dc in directions:
                    row = r + dr 
                    col = c + dc 
                    # now we put the boundary 
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2 # reassign and add to queue 
                    queue.append([row, col])
                    fresh -= 1
                # for every time we pop a rotten off, we increase time?
            time += 1
        return time if fresh == 0 else -1
                

