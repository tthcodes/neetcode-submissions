class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find constraints, any null, 0's, and size of input
        # 10^5 >= ?, 
        # CAN be negative 
        l, r = 0, len(nums) - 1
        res = float('+inf')
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m], nums[l], nums[r])
            if nums[m] > nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res