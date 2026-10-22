class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_obj = {}
        t_obj = {}
        for i in range(len(s)):
            s_obj[s[i]] = s_obj.get(s[i], 0) + 1
            t_obj[t[i]] = t_obj.get(t[i], 0) + 1
        for k in s_obj:
            if s_obj[k] != t_obj.get(k, 0):
                return False
        print(s_obj, t_obj)
        return True


            