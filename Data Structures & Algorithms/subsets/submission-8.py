class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # we want to make sure we return after appending 
        curSet = []
        # add to curSet as long as index is less than nums len

        def backtrack(i): # helper function that walks down nums 
            if i >= len(nums):
                res.append(curSet.copy()) # copy so that we don't append same set
                return 
            # now emulate us taking option
            curSet.append(nums[i])
            # now continue the recursive call 
            backtrack(i + 1)
            # now emulate us taking away that take
            curSet.pop()
            backtrack(i + 1)
        
        # now we want to call back track, return res
        backtrack(0) 
        return res 
