class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sObj, tObj = {}, {}
        for i in range(len(s)):
            sObj[s[i]] = sObj.get(s[i], 0) + 1
            tObj[t[i]] = tObj.get(t[i], 0) + 1
        for c in sObj:
            if sObj[c] != tObj.get(c, 0):
                return False
        return True

