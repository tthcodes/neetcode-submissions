class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init pointers
        l, r = 0, len(nums) - 1
        # start while loop that allows for l = r for when they converge on m
        while l <= r:
            # init m 
            m = (l + r) // 2
            # return m if it meets target
            if nums[m] == target:
                return m
            # if m is in left seq
            if nums[m] >= nums[l]:
                # check if target is greater than nums[m] OR less nums[l], move right 
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: #otherwise target is less than middle AND greater than left, check left
                    r = m - 1
            else: # if m is in right seq
                # check if target is less than nums[m] OR greater than nums[r], check left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: # otherwise target is greater than nums[m] AND less than nums[r], check right
                    l = m + 1
        # otherwise, target doesn't exist
        return -1
                    