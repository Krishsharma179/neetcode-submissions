class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        status=None
        seen1={}
        seen2={}
        set1=set()
        set2=set()
        if len(s)!=len(t):
            return False
        for char in s:
            seen1[char]=1+seen1.get(char,0)
        for char in t:
            seen2[char]=1+seen2.get(char,0)

        for char in s:
            if  seen1.get(char)!=seen2.get(char,0):
                return False
        return True           

                    



            


            

     
        
        