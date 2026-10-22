class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for s in strs:
            length = str(len(s))
            res += length + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        # when i think about doing sliding window and/or two pointer, sometimes i have pause about setting up 2 pointers, or just 1 and using a loop to declare 2nd 

        while l <= len(s) - 1:
            while s[r] != '#':
                r += 1
            
            # once it DOEs hit delimiter, declare length and add
            print(s[l:r])
            length = int(s[l:r]) 
            print(length)
            # slice str and add
            res.append(s[r + 1:r + length + 1]) 
            
            # re-declare L
            l = r + length + 1 
            r = l 

        return res
