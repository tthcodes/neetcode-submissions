class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not the same length, return false
        if len(s) != len(t):
            return False
        # initialize 2 hashmaps
        sObj, tObj = {}, {} 
        # do a for range loop that goes through one of the strings
        for i in range(len(s)):
            # count the number of teams each char shows up in each string w/ respective hashmaps
            sObj[s[i]] = sObj.get(s[i], 0) + 1
            tObj[t[i]] = tObj.get(t[i], 0) + 1
        # iterate over one of the hashmaps, if the value doesn't equal the other return false
        for c in sObj:
            if sObj[c] != tObj.get(c, 0):
                return False
            #we need to do a get() in case it doesn't even exist in the other hash map
        return True