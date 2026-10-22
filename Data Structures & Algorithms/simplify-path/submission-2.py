class Solution:
    def simplifyPath(self, path: str) -> str:
        # conditions to look for, when it's '/'
            # when it's '..' and stack, you pop
            # you ADD whenever cur is NOT '' and cur is NOT JUST '.' 
        # either way, when encountering '/', you clear
        cur = ''
        stack = []
        for c in path + '/': # this ensures you have '/' at the end of iteration to tell you to add the LAST file/directory 
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '.' and cur != '':
                    stack.append(cur)
                cur = ''
            else:
                cur += c
        return '/' + '/'.join(stack)