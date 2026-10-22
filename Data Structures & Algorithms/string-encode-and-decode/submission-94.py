class Solution:

    def encode(self, strs):
        res = ''
        # have to add length + str + delimiter 
        for s in strs:
            res += str(len(s)) + '#' + s
        return res 

    def decode(self, s): 
        res = []
        l = 0
        while l < len(s):
            r = l 
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            res.append(s[r + 1: r + 1 + length])
            l = r + length + 1
        return res
