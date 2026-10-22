class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want to init a str 
        res = ''
        # we want to iterate over each str in strs and also add a delimiter
        for s in strs:
            num = len(s)
            res = res + str(num) + ':' + s
        return res

    def decode(self, s: str) -> List[str]:
        # start a left pointer 
        l = 0
        # init a res list
        res = []
        while l < len(s):
            r = l
            while s[r] != ':':
                r += 1
            length = int(s[l:r])
            res.append(s[r + 1: r + length + 1])
            l = r + 1 + length
        return res