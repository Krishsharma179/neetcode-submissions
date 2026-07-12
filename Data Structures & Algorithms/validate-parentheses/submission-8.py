class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={}
        
    
        #This is close to open

        hashmap["}"]="{"
        hashmap[")"]="("
        hashmap["]"]="["

        for i in  s :
            if i in hashmap:
                if stack and stack[-1]==hashmap[i]:
                    stack.pop()
                else:
                    return False    

            else:
                stack.append(i)    

        if not stack and len(stack)<1:
            return True
        else:
           return  False     
        
        # print(stack)    

# So it is like it will check for the character in s and if it is a open bracket it will append it to the 
# stack and if it a closing bracte it will check the -1 and if it is == return true
        
               
        
         


        