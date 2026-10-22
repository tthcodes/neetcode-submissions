class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset because they only keep unique elements 
        # make two hashmaps, iterate of either hashmap and compare to the other
        # if theres a match, add it to the hashset
        res = set()
        oneMap, twoMap = {}, {}
        for n in nums1:
            oneMap[n] = oneMap.get(n, 0) + 1
        for n in nums2:
            twoMap[n] = twoMap.get(n, 0) + 1
        for n in oneMap:
            if n in twoMap:
                res.add(n)
        print(oneMap, twoMap)
        print(res)
        return list(res)