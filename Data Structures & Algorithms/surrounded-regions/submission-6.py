class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #input: list[list[str]] 
        #output: None 

        '''
        i think what we can do is we can init a visited set
        then we can start the search from the outer edges, and for all regions that already touch the edge, we can add them to visited without 'flipping them' 

        then we can go ahead and flip all other regions we see after that 
        '''

        rows = len(board)
        cols = len(board[0]) 

        # init visited set
        visited = set()

        # helper function to dfs

        def dfs(r, c, action):
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if cr < 0 or cr >= rows or cc < 0 or cc >= cols or board[cr][cc] == 'X' or (cr, cc) in visited:
                    continue
                
                visited.add((cr, cc))
                if action == 'capture':
                    board[cr][cc] = 'X'
                # instead of recursing, push 4 neighbors onto stack to visit
                stack.append((cr + 1, cc))
                stack.append((cr - 1, cc))
                stack.append((cr, cc + 1))
                stack.append((cr, cc - 1))

        # but how do i make it so that dfs can change the grid in place for the 2nd run through after having visited the edge regions? maybe add another param
        # now we want to run through edges 
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0, 'visit')
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1, 'visit')

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c, 'visit')
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c, 'visit')

        # now iterate through whole thing and only turn non-visited regions to captured
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    dfs(r, c, 'capture')

        return None
