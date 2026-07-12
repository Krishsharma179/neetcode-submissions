class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0 #initializing both the pointers 
        subs=1
        if s==" " or s=="":
            return len(s)
    
        while r<=len(s)-2 and l<=len(s)-2:
            r+=1
            i=l
            while i<r:
                if s[i]==s[r]:
                    l=i+1
                i+=1    
            
            subs=max(subs,r-l+1)
            
                 

        return subs        

        