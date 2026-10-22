class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
                # input: m = num of rows (int), n = num of cols (int)
        # output: int (num of unique paths) 

        # build out graph 
        graph = [[1] * n for _ in range(m)]

        # now we can iterate from 2nd to last col and row, and add bottom and right
        for r in range(m - 2, -1, -1): #start from 2nd to last to not go out of bounds
            for c in range(n - 2, -1, -1 ):
                graph[r][c] = graph[r + 1][c] + graph[r][c + 1]

        return graph[0][0]
