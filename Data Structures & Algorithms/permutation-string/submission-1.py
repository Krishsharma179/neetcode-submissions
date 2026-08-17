class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False
            
        l=0                  
        r=len(s1)-1

        s1_h={}

        for i in s1:
            if i in s1_h:
                s1_h[i]+=1
            else:
                s1_h[i]=1    

        while r < len(s2):
            hashmap={}
            for i in s2[l:r+1]:
                if i in hashmap:
                    hashmap[i]+=1
                else:
                    hashmap[i]=1

            if hashmap==s1_h:
                return True

            l+=1
            r+=1    
                         
        return False   
            
            



                     


            
            
