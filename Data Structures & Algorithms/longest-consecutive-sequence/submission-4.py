class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        input: int list (nums)
        output: int (length)

        create a set out of the nums, which would order it, as well as get rid of duplicates, puts us at O(N) time
        then iterate over the set checking if there is a lesser number by 1 already in the set. if not, we know it's a beginning of a new sequence 
        once the beginning of new sequence begins, we begin the count, and return the max 
        '''
        res = 0
        
        numSet = set(nums)

        for n in numSet:
            if n - 1 not in numSet:
                # begin new seq 
                curSeq = 1
                while n + 1 in numSet:
                    curSeq += 1
                    n += 1 
                res = max(res, curSeq)
        
        return res
