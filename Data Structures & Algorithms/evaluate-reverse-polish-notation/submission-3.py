class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        # operators={'+': +, '-':-, '*':*,'/':/}
        output=0

        # What i will do is put the no.s in the stack and whenever it is any operator I will add ot 

        for i in tokens:
            if i == '+':
                a,b=stack.pop() , stack.pop()
                stack.append(a+b)
            elif i == '-':
                a,b=stack.pop() , stack.pop()
                stack.append(b-a)
            elif i == "*":
                a,b=stack.pop() , stack.pop()
                stack.append(a*b)
            elif i == "/":
                a,b=stack.pop() , stack.pop()
                stack.append(int(float(b)/a))

            else:
                stack.append(int(i))
                print(stack)            

        return stack[0]      