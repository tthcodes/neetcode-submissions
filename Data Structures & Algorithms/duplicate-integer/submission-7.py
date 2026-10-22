class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # add to a set? 
        # hashset 
        # compare lens
        uniqueNums = set(nums)
        if len(uniqueNums) != len(nums):
            return True
        else:
            return False