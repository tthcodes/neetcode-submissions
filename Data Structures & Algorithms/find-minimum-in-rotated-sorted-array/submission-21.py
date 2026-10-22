class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            m = (l + r) // 2
            
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # if m is part of left sequence 
            if nums[m] >= nums[l]:
                # we want to check the right sequence for possible smaller nums
                l = m + 1
            
            else: # else if m is part of right sorted seq, check left 
                r = m - 1
            
            # either way, grab min of nums[m], res

            res = min(nums[m], res)
        
        return res