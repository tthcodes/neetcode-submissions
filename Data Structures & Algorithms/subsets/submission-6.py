class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # input: a list of int's
        # outut: a list of all possible subsets (list of lists)
        res = [] 
        curSet = []  # do i put this curSet in or out of recursive call?.. you want to keep track of INDEX so you can move it along in the recursive call. 

        def backtrack(i):
            # you want to return whenever i >= len(nums)
            if i >= len(nums):
                res.append(curSet.copy())
                return
            
            # now you want to create the 2 possibilities, then move along 
            curSet.append(nums[i]) 
            backtrack(i + 1)
            
            curSet.pop()
            backtrack(i + 1)
        
        # now i is constantly increasing as it moves along nums, and curSet is experiencing each possibility of takes/no takes until i is greater than len(nums), stopping the recursive call.

        # dry run [1, 2, 3] -> [[], [1], [2] … etc. ]

        # you want to think of the recursive call as doing the decision to take it, then doing the decision of NOT taking it, which is possiblie by popping. 

        backtrack(0) # start at 0
        return res
