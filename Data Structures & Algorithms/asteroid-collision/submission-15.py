class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]: 

        stack = []

        for i in asteroids:

            if i > 0:
                stack.append(i)

            else:

                while stack and stack[-1] > 0:

                    if abs(stack[-1]) == abs(i):
                        stack.pop()
                        break

                    elif abs(stack[-1]) < abs(i):
                        stack.pop()
                    else:
                        break     

                else:
                    stack.append(i)

        return stack                       
        

        