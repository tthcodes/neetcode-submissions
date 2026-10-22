class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tObj = {}
        sObj = {}
        for char in s:
            tObj[char] = tObj.get(char, 0) + 1
        for char in t:
            sObj[char] = sObj.get(char, 0) + 1
        for key, val in tObj.items():
            if sObj.get(key, 0) != val:
                return False
        return True