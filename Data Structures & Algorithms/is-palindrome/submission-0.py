class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2="".join(filter(str.isalnum,s))
        s=s2.replace(" ","").lower()
        
        forward=0          #front index
        backward=len(s)-1      #last index

        while(forward<backward):
            if s[forward]!=s[backward]:
                return False

            forward+=1
            backward-=1

        return True        


        