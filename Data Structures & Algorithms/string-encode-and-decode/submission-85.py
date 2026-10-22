class Solution:

    def encode(self, strs: List[str]) -> str:
        print('HELLO')
        res = ''
        # we want to include the int len + divider + actual st r
        for s in strs:
            res += str(len(s)) + '/' + s
        return res

    def decode(self, s: str) -> List[str]:
        print('HELLO')
        res = []
        # use a pointer, and the while loop will initiate a secondd
        l = 0
        while l < len(s):
            print('hi!')
            # init second pointer 
            r = l
            # move the second pointer until it hits the divider to find str len
            while s[r] != '/':
                r += 1
            # take out the length
            length = int(s[l:r])
            # add the str to the list
            res.append(str(s[r + 1 : r + 1 + length]))
            # you want to move the l to last index of the move, since the move is exclusive at end
            l = r + 1 + length
        return res