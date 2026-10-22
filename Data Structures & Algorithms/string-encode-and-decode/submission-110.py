class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s

        return res


    def decode(self, s: str) -> List[str]:
        res = []

        l, r = 0, 0

        while l <= len(s) - 1:
            # now we move r till it hits the first delimiter
            while s[r] != '#':
                r += 1
            # now we parse out the length 
            length = int(s[l:r]) 
            
            # and then append to res 
            res.append(s[r + 1: r + 1 + length])
            
            # then we must re-assign l, r + 1 + length should be the beginning of next length
            l = r + 1 + length 
            r = l

        return res 
