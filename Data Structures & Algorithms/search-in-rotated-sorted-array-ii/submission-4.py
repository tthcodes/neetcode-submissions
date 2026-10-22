class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # has duplicates, so defining edge and what side M is on will be a challenge
        # init our pointers 
        l, r = 0, len(nums) - 1

        # start while loop
        while l <= r:
            # init midpoint
            m = (l + r) // 2

            # return true if target found
            if nums[m] == target:
                return True
            
            # find where midpoint is left or right sorted side
            # to do this, we need to keep sliding left border until it's different from midpoint
            if nums[l] == nums[m]:
                l += 1
                continue
                # this re-establishes m everytime until left not on a duplicate 
            
            # now we find which side m is and search accordingly based on relation to target
            if nums[l] <= nums[m]: # if l <= m, we know it's part of left sort of current subaray
                # now we find reference for target
                if nums[l] <= target < nums[m]: # if it's inbounds between l and m, look left 
                    r = m - 1
                else: # else move right
                    l = m + 1
            
            else: # else nums[l] > m, so it's on right sorted portion.
                if nums[m] < target <= nums[r]: # if target is between m and r, look right
                    l = m + 1
                else: # else move left
                    r = m - 1
            
        # if it's not found and borders cross each other, return false
        return False