class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curDir = ''
        for s in path + '/':
            if s == '/':
                if curDir == '..':
                    if stack: stack.pop()
                elif curDir != '' and curDir != '.':
                    stack.append(curDir)
                curDir = ''
            else:
                curDir += s
        return '/' + '/'.join(stack)


            
