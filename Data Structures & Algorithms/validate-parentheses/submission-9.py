class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]


        output = False 
        
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in s:
            if i in dic.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack.pop() != dic[i]:
                    return False
                
                
        
        
        if len(stack) != 0:
            return False
        else:
            return True 
        