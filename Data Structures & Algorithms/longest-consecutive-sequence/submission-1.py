class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need O(N) time, so no sort 
        res = 0
        setNums = set(nums)
        for n in setNums:
            curSeq = 1
            while n - 1 in setNums:
                curSeq += 1
                n -= 1
            res = max(res, curSeq)
        return res