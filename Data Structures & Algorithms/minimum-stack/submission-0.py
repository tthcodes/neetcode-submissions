class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # stores the min at each iteration of the stack 

    def push(self, val: int) -> None:
        self.stack.append(val)

        # now we need to update the minStack. if the top of the minStack is > val OR there is no minStack, push val onto minstack. 
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else: # alternatively, minstack exists and val is >= top of minstack, re-add minstack top 
            self.minStack.append(self.minStack[-1])

        

    def pop(self) -> None:
        # remove top el from both stacks
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
