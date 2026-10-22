class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + ":" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            print('error')
            j = i
            while s[j] != ":":
                j += 1
            word_count = int(s[i:j])
            res.append(s[j + 1 : j + 1 + word_count])
            i = j + 1 + word_count
        return res