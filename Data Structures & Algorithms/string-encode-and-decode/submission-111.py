class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        # iterate through until we find the delimeter, then isolate the length
        while l < len(s):
            j = l
            while s[j] != '#' and j < len(s):
                j += 1
            length = int(s[l:j])
            res.append(s[j + 1:j + 1 + length])
            l = j + 1 + length
        return res


