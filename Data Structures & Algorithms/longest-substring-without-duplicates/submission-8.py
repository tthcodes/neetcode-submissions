class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need a sliding window that is able to grow if there are no duplicates within it
        # init a max num
        res = 0
        # initialize a left pointer, and have the right pointer as the loop
        l = 0
        # init a hashset 
        longestSub = set()
        for r in range(len(s)):
            while s[r] in longestSub:
                longestSub.remove(s[l])
                l += 1
            longestSub.add(s[r])
            res = max(res, len(longestSub))
        return res

