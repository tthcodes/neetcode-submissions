class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            # we need to add letter count per s
            res += str(len(s)) + ':' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        # '4:word'
        # init pointer
        i = 0
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            count = int(s[i:j])
            res.append(s[j + 1 : j + 1 + count])
            i = j + 1 + count
        return res