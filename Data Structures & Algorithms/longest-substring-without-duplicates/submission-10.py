class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dynamic sliding window
        # initiliaize left border 
        l = 0
        # init hashset
        subStr = set()
        # ini longestSubLength
        longestSubLen = 0
        # for loop for right pointer
        for r in range(len(s)):
            while s[r] in subStr:
                subStr.remove(s[l])
                l += 1
            # add the current right pointer char
            subStr.add(s[r])
            # increment r
            longestSubLen = max(longestSubLen, len(subStr))
        return longestSubLen
