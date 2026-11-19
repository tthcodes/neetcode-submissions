class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sorted originally ascending, but rotated. 
        # o log n, suggests binary search 

        # init pointers 
        l, r = 0, len(nums) - 1

        # check if the the list is already ordered, if so proceed binary search as is
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                    return m
            
            # the part we need to nail down is getting it WITHIN a band 
            if nums[l] < nums[r]:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # now we need to check which side is ordered 
            if nums[l] <= nums[m]: # if left side is ordered... right side unordered 
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else: # right side ordered
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
