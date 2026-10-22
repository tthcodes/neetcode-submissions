class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list of int's
        # we want to return a list, where each nums[n] is the product of every other
        # we want to make use of prefix and postfixes.
        pre, post = 1, 1 

        # we want to make a new res 
        res = [1] * len(nums) # should return [1, 1, 1, 1] something like this

        # we can probably do 2 loops one forward, one backward that tells us pre and post
        # this should utilize pre and create it as it updates res.
        for i, n in enumerate(nums):
            res[i] *= pre 
            pre *= n

        # then we can do the same for post
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        # then we can resturn res 
        return res
