class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # init res
        res = []
        # sort the nums
        nums.sort()
        for i in range(len(nums)):
            # we want to skip duplicates 
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # init pointeres
            l, r = i + 1, len(nums) - 1
            # init while loop
            while l < r:
                # init sum
                curSum = nums[l] + nums[r] + nums[i]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[i], nums[r]])
                    # and then we want to move either of the pointers WHILE making sure there are no repeat numbers
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res