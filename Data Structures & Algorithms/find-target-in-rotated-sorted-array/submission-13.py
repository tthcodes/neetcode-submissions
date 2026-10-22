class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2 
            if nums[m] == target:
                return m
            
            # now we need to check which side m is in

            if nums[m] < nums[l]: # if it is on the the right non-sorted side
                # check outer boundaries for this
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1 
            else:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1