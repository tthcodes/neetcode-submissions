class Solution:

    def encode(self, strs: List[str]) -> str:
        # init res str
        res = ""
        # iterate through each str
        for s in strs:
            # add length + delimiter + actual str
            res += str(len(s)) + ':' + s
        # return output str
        return res

    def decode(self, s: str) -> List[str]:
        # init output list 
        res = []
        # init first pointer, i
        i = 0
        # while loop for as long as i < input str
        while i < len(s):
            j = i
            # while loop that increments j until delimiter is found
            while s[j] != ":":
                j += 1
            # take out length 
            length = int(s[i:j])
            # append the word using length
            res.append(s[ j + 1 : j + 1 + length ])
            # reassign i 
            i = j + length + 1
        return res