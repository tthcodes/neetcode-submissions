class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input: str of lowercase letters 
        output: int, longest substring without duplicates

        init a set, and init 2 pointers. move right pointer along and keep adding to set, and update highest length of this set. once right pointer runs into a duplicate, you move left pointer along and remove each letter until right pointer letter no longer in set. continue
        '''

        res = 0
        setChars = set()

        l = 0

        for r in range(len(s)):
            if s[r] not in setChars:
                setChars.add(s[r])
                res = max(res, len(setChars))
            else:
                while s[r] in setChars:
                    setChars.remove(s[l])
                    l += 1
                setChars.add(s[r])
        
        return res
