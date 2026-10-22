class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res 
        res = []
        # sort 
        nums.sort()
        # iterate, holding onto value and index using enumerate
        for i, n in enumerate(nums):
            # continue the iteration if there is a duplicate and i > 0
            if i > 0 and n == nums[i - 1]:
                continue
            # else, begin 2 pointers and check sums
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + n
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    # need to move l, while also making sure it isn't a duplicate
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res