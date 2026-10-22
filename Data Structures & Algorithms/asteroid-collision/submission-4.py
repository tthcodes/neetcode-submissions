class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # init a stack
        stack = [] # this stack lets us move left to right.
        # NOTE: + = right, - = left 
        # iterate over the asteroids
        for a in asteroids:
            # we want to check if there is a collision
            # collision condition: top of stack is +, and a is -.. 
            # we want it to be a while condition in the case top of stack is destroyed
            while stack and stack[-1] > 0 and a < 0:
                # now we want to compare when either is greater or equal
                if abs(a) > stack[-1]:
                    stack.pop()
                    # and we don't set to 0, because if we did we wouldn't append
                elif abs(a) < stack[-1]:
                    # in this scenario, we set a to 0, don't append
                    a = 0
                    # this also allows us to break the while loop
                else:
                    # in the case they're equal
                    stack.pop() # remove positive top of stack
                    a = 0 # set a to 0 and don't append
            # this now occurs after all collisions have happend
            if a: # if a is not a null value
                stack.append(a)
        return stack