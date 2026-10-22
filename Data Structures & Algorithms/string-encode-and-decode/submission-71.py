class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + ':' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            # encompass the length of the word using delimiter
            j = l
            while s[j] != ':': # while it isn't at the delimiter
                j += 1
            # declare length
            length = int(s[l:j])
            # move to encompass whole word
            res.append(s[j + 1:j + 1 + length])
            # move l to next length 
            l = j + length + 1
        print(res)
        return res
