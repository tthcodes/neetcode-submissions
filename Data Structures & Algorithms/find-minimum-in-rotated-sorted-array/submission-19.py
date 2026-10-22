class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2

            # check if in order 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            
            # now that we know it's not in order, check which seq M in
            if nums[m] < nums[l]: # if in right sorted side, we know left side has smaller
                # set new min
                r = m - 1
            else:
                l = m + 1

            res = min(res, nums[m])
        return res