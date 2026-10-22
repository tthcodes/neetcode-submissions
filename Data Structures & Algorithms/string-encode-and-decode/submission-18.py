class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ''
        for string in strs:
            encodeStr += str(len(string)) + '#' + string 
        return encodeStr

    def decode(self, str) -> List[str]:
        res, i = [], 0 #pointer to begin at str
        while i < len(str): #while loop to iterate over long str
            j = i #2nd pointer to diff between word and word count integer
            while str[j] != "#": #moving JUST the 2nd pointer until added delimiter found
                j += 1
            #once delimiter found, init length var by turning str from i:j into INT
            length = int(str[i:j]) #this isolates your added count for word, and doesn't include delimiter
            res.append(str[j + 1 : j + 1 + length]) 
                #append slice from char RIGHT AFTER delimiter, to char after word count + 1
            i = j + 1 + length
        return res

