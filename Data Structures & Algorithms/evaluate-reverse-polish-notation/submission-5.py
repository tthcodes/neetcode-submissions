class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        init a stack to hold previous numbers
        for each operator, perform the operation, and put the result to top of stack
        return last remaining num on stack as res 
        '''
        stack = []
        for t in tokens:
            if t == '+':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num1) + int(num2))
            elif t == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2) - int(num1))
            elif t == '*':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2) * int(num1))  
            elif t == '/':
                # what is it that makes a division result go to floor of 0?
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int((int(num2) / int(num1))))
            else:
                stack.append(t)
        return int(stack[-1]) if stack else None