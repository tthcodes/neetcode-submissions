class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if they have same length
        if len(s) != len(t):
            return False
        # init two dicts to store char and count
        sDict, tDict = {}, {}
        # for loop to populate each dict
        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        # iterate through one of the dicts and compare to other
        for c in sDict:
            if sDict[c] != tDict.get(c, 0):
                return False
        # return true if they match
        return True