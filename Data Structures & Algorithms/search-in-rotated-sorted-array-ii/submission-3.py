class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # now there are duplicates, so you can't rely on 
        # finding m using nums[l] <= nums[m] being left side.
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            # if you find target return truye
            if nums[m] == target:
                return True
            
            # shift left until you find a number that != nums[m]
            if nums[l] == nums[m]:
                l += 1
                continue
            
            
            # NOW you can tell if it's part of left order or not
            if nums[l] <= nums[m]: # if left ordered
                if nums[m] > target >= nums[l]:
                    # go left 
                    r = m - 1
                else:
                    # go right
                    l = m + 1
            else: # right ordered
                if nums[m] < target <= nums[r]:
                    # go right 
                    l = m + 1 
                else:
                    r = m - 1

        return False
