class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find constraints, any null, 0's, and size of input
        # 10^5 >= ?, 
        # CAN be negative 
        res = float('+inf')
        l, r = 0, len(nums) - 1
        # important thing to note is realizing what part of the order the midpoint is in, then search the OTHer side
        while l <= r:
            # case for when it's IN order 
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # if midpoint is greater than R, it's in that order, look at right side
                l = m + 1
            else: 
                r = m - 1
        return res
            