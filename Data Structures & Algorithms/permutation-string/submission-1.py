class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        we need to create 2 dicts, one containing the comparison str, and the other keeping track of the currently searched substring 

        while iterating and updating the 2nd dict, if it ever equals the first, return true. if not, false
        '''
        strMap = Counter(s1)

        subMap = {}

        l = 0

        for r in range(len(s2)):
            subMap[s2[r]] = subMap.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                subMap[s2[l]] -= 1
                if subMap[s2[l]] == 0:
                    del subMap[s2[l]]
                l += 1
            if subMap == strMap:
                return True
        
        return False