class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ordNums = sorted(nums)
        for i in range(len(ordNums)):
            if i > 0 and ordNums[i] == ordNums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                lnum, mnum, rnum = ordNums[l], ordNums[i], ordNums[r]
                curSum = lnum + mnum + rnum
                if curSum == 0:
                    res.append([lnum, mnum, rnum])
                    l += 1 
                    while ordNums[l] == ordNums[l - 1] and l < r:
                        l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    l += 1
        return res

