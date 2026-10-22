class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # it's sorted by increase
        # we return index of target, not target
        # can use target to move left or right 
        # we want to be searching out of bounds, not in bounds
        l, r = 0, len(nums) - 1
        while l <= r:
            
            m = (l + r) // 2

            # return index if it matches

            if nums[m] == target:
                return m
            
            # else we didn't find m yet, figure out which side m is on

            if nums[m] >= nums[l]: # if M greater or equal to l bound, it's left sorted
                # if we're in left seq, we need to move it depending on M's val relaeted to left bound or target
                
                # INBOUND VERSION
                if nums[l] <= target < nums[m]: # if target greater than or equal to L + less than M, go left
                    r = m - 1
                else:
                    l = m + 1
            
            else: # else M is less than L, it's part of right seq

                if nums[r] >= target > nums[m]: # if target equal to or less than R and larger than M, go right
                    l = m + 1
                else:
                    r = m - 1
        # otherwise return -1

        return -1
