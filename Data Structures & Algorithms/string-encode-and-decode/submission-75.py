class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want to init a str 
        res = ''
        # we want to iterate over each str in strs and also add a delimiter
        for s in strs:
            res = res + s + '-'
        return res

    def decode(self, s: str) -> List[str]:
        # start a left pointer 
        l = 0
        # init a res list
        res = []
        r = 0
        print(len(s))
        print(s)
        while r < len(s):
            if s[r] != '-':
                r += 1
                continue
            else:
                print('gets here')
                res.append(s[l:r])
                l = r + 1
                r += 1
        return res