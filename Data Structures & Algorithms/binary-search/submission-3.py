class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search is an implementation of two pointers 
        l, r = 0, len(nums) - 1
        # find a middle
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1