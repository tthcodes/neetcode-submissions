class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # input: array of nums
        # output: array of arrays 

        # output is ALL possible combinations of a subset. 
        res = []
        curSet = [] 

        def dfs(start):
            # if start is >= len(nums), append and return 
            if start >= len(nums):
                res.append(curSet.copy())
                return
            
            curSet.append(nums[start])
            dfs(start + 1)
            curSet.pop()
            dfs(start + 1)

        dfs(0)

        return res
