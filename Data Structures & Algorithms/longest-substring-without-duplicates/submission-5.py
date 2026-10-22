class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case for when len(s) is 0 or 1
        if len(s) == 0 or len(s) == 1:
            return len(s)
        # init substr
        longestSub = 0
        for i in range(len(s) - 1):
            currSub = 0
            subSet = set()
            j = i
            print(s[j])
            while j < len(s) and s[j] not in subSet:
                subSet.add(s[j])
                currSub += 1
                j += 1
            if currSub > longestSub:
                longestSub = currSub
        return longestSub
        

