from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init res
        res = []
        # bucket sort technique
        # how do we count how many of each? counter hashmap 
        freqCount = Counter(nums)
        # now we want to create a bucket sort list, where the length is the same as nums + 1, so we have a 0 count, to account for 0-index 
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqCount.items():
            bucket[freq].append(num)
        # now we can iterate from the end of bucket and return res 
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res