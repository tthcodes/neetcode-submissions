class Solution:

    def encode(self, strs: List[str]) -> str:
        #init res str
        encodeStr = ''
        #iterate over strings of input list
        for string in strs:
            encodeStr += str(len(string)) + '#' + string 
            #encode word by adding its length number + delimiter + actual str
            #delimiter btwn word count and string gets rid of needing to worry if same delimiter in actual string
        return encodeStr

    def decode(self, str) -> List[str]:
        res, i = [], 0 #init result arr, init 1st pointer to begin at str
        while i < len(str): #while loop to iterate over chars of long str
            j = i #2nd pointer to identify word count
            while str[j] != "#": #moving JUST the 2nd pointer until added delimiter found
                j += 1
            #once delimiter found (j = #), init length number var by turning str from i:j into INT
            length = int(str[i:j]) #this isolates your added count for word, and doesn't include delimiter
            res.append(str[j + 1 : j + 1 + length]) 
                #append slice from char RIGHT AFTER delimiter, to char (after word count length)
            i = j + 1 + length 
                #now move on to next word, by moving 1st pointer to beginning of word count of next word
        return res

