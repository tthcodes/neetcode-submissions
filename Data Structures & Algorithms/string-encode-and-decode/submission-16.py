class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ''
        for string in strs:
            encodeStr += str(len(string)) + '#' + string 
        return encodeStr

    def decode(self, str) -> List[str]:
        res, i = [], 0

        while i < len(str):
            print('current str:', str[i])
            j = i 
            while str[j] != "#":
                j += 1
            print('current j:', j)
            print(str[i:j])
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length]) 
            i = j + 1 + length
        return res

