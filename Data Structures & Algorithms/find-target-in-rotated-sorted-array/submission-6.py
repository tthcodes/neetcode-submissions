class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # check what seq m belongs to
            if nums[l] <= nums[m]: # if it's in right order, we wanna check if target is less than right
                if target > nums[m] or target < nums[l]: # if target is greater than m, go right
                    l = m + 1
                else: # otherwise if target is less than middle OR target is greater than nums[l], go left
                    r = m - 1 
            else: #if it's in wrong order side
                if target < nums[m] or target > nums[r]: # and if target is less than middle or target greater than right-most, go left 
                    r = m - 1
                else: # else if target is greater than middle OR target is less than rightmost, go right
                    l = m + 1
        return -1