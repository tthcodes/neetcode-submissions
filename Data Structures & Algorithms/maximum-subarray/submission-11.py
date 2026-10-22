class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # input: list of ints
        # output: int, largest continuous subarray sum 

        # init a res
        res = nums[0] 

        # continue to keep curSum until it turns negative 
        curSum = 0

        # when it turns negative, we'll set it to the current num we're on, and we'll compare max between curSum and res with every step 

        # this should make time complexity O(N), space complexity O(1), since we only hold variables set to ints 

        for n in nums:
            curSum += n
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0

        return res
