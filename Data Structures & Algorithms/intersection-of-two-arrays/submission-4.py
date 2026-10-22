class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashset because they only keep unique elements 
        # make two hashmaps, iterate of either hashmap and compare to the other
        # if theres a match, add it to the hashset
        res = []
        if len(nums1) > len(nums2):
            twoSet = set(nums2)
            for n in nums1:
                if n in twoSet:
                    res.append(n)
                    twoSet.remove(n)
        else:
            oneSet = set(nums1)
            for n in nums2:
                if n in oneSet:
                    res.append(n)
                    oneSet.remove(n)
        return res