class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        L = 0 
        R = 0 
        count = 0
        res = 0
        freq = {}
        

        

        while  R < len(s):
            
            
            if s[R] in freq:
                freq[s[R]] += 1
            else:
                freq[s[R]] = 1

            count = max(freq.values())   
            
            

            while (R - L + 1) - count > k :
                freq[s[L]] -= 1
                L +=1 
            
            res = max(res , R-L+1)
            
            R+=1


        return res        

            

            


        