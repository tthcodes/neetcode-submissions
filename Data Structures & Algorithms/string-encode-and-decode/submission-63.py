class Solution:

    def encode(self, strs: List[str]) -> str:
        # have a way to put in a number to rep how many letters in next word
        # have a way to put in separator
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return output


