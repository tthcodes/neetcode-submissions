class Solution:

    def encode(self, strs: List[str]) -> str:
        #create an empty str that u will put list of strings into
        res = ""
        #iterate over list of str's 
            #add current word count + delimiter + actual word
        for string in strs:
            count = str(len(string))
            res += count + ":" + string
        return res

    def decode(self, s: str) -> List[str]:
        #init list
        res = []
        #use 2 pointers to isolate the word str
        i = 0 #pointer 1
        #iterate over input string
        while i < len(s):
            j = i #start pointer 2 at pointer 1
            while s[j] != ":":
                j += 1
            strCount = int(s[i:j])
            res.append(s[j + 1 : j + 1 + strCount])
            i = j + 1 + strCount
        return res