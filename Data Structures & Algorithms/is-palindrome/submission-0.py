class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we'll need isalnum()
        # establish two pointer
        # if match, move each by one
        # do a while loop so that they don't cross each other
        l, r = 0, len(s) - 1
        while l < r:
            #check if left pointer isalnum
            #if not, move it to the right and continue loop
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True