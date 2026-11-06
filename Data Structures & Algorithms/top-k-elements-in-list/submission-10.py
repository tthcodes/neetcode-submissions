class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        input: int list (nums)
        output: int list (k most frequent digits in nums)

        - look up what the brute force method would be. i would first start with making a Counter() of the nums, and then somehow sorting it by frequency, then iterate through the dict and append the value to a res list until len(res) == k. but i'm not sure how I'd even sort a dict by its freq or if that's even a thing. 
        optimal way is to use bucket sort algorithm. trick to watch for is the have the length of the bucket to be + 1 of the actual len of nums to account for out of range error, this way even if all nums are the same, it can still be placed appropriately. 
        we can still user the Counter() method to populate a dict, then iterate over the Count to populate bucket sort. then we iterate backward from end of the bucket to populate a res list up to k.
        '''
        res = []
        numCount = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        # iterate over count
        for num, freq in numCount.items():
            bucket[freq].append(num)
        
        # iterate backward over bucket 
        for freq in range(len(bucket) - 1, -1, -1):
            for n in bucket[freq]:
                if len(res) == k:
                    return res
                res.append(n)
        return res