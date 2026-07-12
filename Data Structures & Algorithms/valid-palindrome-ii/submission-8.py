class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        def checkplaindrome(s):
            l=0
            r=len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True


        while i<j:
            if s[i] != s[j]:
                s1=s.replace(s[i],"",i)
                s2=s.replace(s[j],"",j)
                print(s1)
                print(s2)
                return checkplaindrome(s1) or checkplaindrome(s2)

            else:
                i+=1
                j-=1    
        return True




