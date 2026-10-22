class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2 
            if nums[m] == target:
                return m
            
            # now we need to check which side m is in

            if nums[m] < nums[l]: # if it is on the the right non-sorted side
                # we need to check if m is greater than target or if target is less than rightmost
                if target > nums[m] and target <= nums[r]: # check right if so
                    l = m + 1
                else: # else if target is less than M or target is greater than rightmost, check left
                    r = m - 1
            
            else: # else if m is in sequence 
                if target < nums[m] and target >= nums[l]: # if target between l and m, check left 
                    r = m - 1
                else: # elif target is greater than M or less than nums[l], check right side
                    l = m + 1
        
        return -1