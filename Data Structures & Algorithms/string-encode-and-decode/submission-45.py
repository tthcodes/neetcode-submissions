class Solution:

    def encode(self, strs: List[str]) -> str:
        #init str
        longStr = ""
        #iterate over input list, and add them onto longStr, with word count of each and delimiter
        for string in strs:
            longStr += str(len(string)) + ":" + string
        return longStr

    def decode(self, s: str) -> List[str]:
        #init res list
        res = []
        #utilize 2 pointers to isolate word count vs. delim vs. word
        #init 1st pointer
        i = 0
        #loop over char of strings
        while i < len(s):
            #init 2nd pointer, starting at i, so it can move with i
            j = i
            while s[j] != ":": #while loop to increment 2nd pointer until it becomes delimiter
                j += 1
            #isolate word count, turn it into int
            str_count = int(s[i:j]) #exclude delimiter
            #append actual str using str_count and j.
            print(j)
            res.append(s[j + 1 : j + 1 + str_count]) # plus 1 to start at first char right of delim + include last char of word
            #move i along str
            i = j + 1 + str_count
        return res