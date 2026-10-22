class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we need to find frequency of each num
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        # now it's populated, we can do a bucket sort, create bucket len of NUMS len. not sure if I need to + 1 to account for 0 frequency. i don't think so.

        bucket = [[] for _ in range(len(nums) + 1)] # this should give 1 more el than len(nums), which is needed in case ALL nums are same. if there's 5 1's in nums, and we look for 5th index, it'll go beyond index if we don't add + 1.. 
        
        # loop over hamp to populate bucket sort
        for key, val in hmap.items():
            bucket[val].append(key)
        # init res 
        res = []
        # now we want to iterate from the end of hmap for k amount
        for i in range(len(bucket) - 1, -1, -1): 
            curBucket = bucket[i]
            for n in curBucket:
                print(len(res), k)
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        # return res
        return res 
