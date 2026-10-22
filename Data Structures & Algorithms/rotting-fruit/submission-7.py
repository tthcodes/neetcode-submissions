class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we want to return minimum num of minutes that elapsed till no cell has fresh orange
        # IF fresh orange is walled off, we return -1 
        # we want to init the needed outer variables
        fresh = 0
        time = 0
        queue = deque() # will be adding each rotten position here 
        rows = len(grid)
        cols = len(grid[0]) 

        # init list of directional positions to create a col/row diff, to infect surroundings 
        # we'll iterate over this to place next cells. but we'll check boundaries before moving to them
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # now we can iterate of grid and populate 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1 

        # now that we've iterated over and counted fresh and appended to queue, we can infect, but what's the condition? i think it should just be while the queue exists
        while len(queue) and fresh:
            # now we make a loop that captures current rotten oranges
            for _ in range(len(queue)):
                r, c = queue.popleft()
                # now that we have r, c we can conditionally infect
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc 
                    if row < 0 or row > rows - 1 or col < 0 or col > cols - 1 or grid[row][col] != 1:
                        continue
                    else:
                        grid[row][col] = 2 
                        queue.append([row, col])
                        fresh -= 1
            # after each loop of current queue len, increase time by 1
            time += 1

        # then after queue is done infecting all it can, return time if fresh == 0
        return -1 if fresh else time
