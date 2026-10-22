class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # input: int list 
        # output: int, max subarray 

        '''
        we want to keep a curSum initialized at 0, and we can start the res at the first num 

        time: O(N) n being how many nums in nums
        space: O(1), we're only holding on to int's 
        '''

        res = nums[0]

        curSum = 0

        for n in nums:
            # make sure that res gets to check both curSum and res BEFORE re-setting curSum to 0
            curSum += n
            
            res = max(res, curSum)
            
            if curSum < 0:
                curSum = 0

        return res 
