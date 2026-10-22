class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            if (nums[l] * nums[l]) > (nums[r] * nums[r]):
                res.append(nums[l] * nums[l])
                l += 1
            elif (nums[r] * nums[r]) > (nums[l] * nums[l]):
                res.append(nums[r] * nums[r])
                r -= 1
            elif l == r:
                res.append(nums[r] * nums[r])
                r -= 1
            elif (nums[r] * nums[r]) == (nums[l] * nums[l]):
                res.append(nums[r] * nums[r])
                res.append(nums[l] * nums[l])
                r -= 1
                l += 1
        return res[::-1]

