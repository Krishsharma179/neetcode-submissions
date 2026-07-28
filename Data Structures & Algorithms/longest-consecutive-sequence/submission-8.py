class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        size=1

        l=0
        r=0

        if len(nums)==0:
            return 0


        nums=sorted(set(nums))     
        
        print(nums)

        while r < len(nums)-1:

            if nums[r+1]-nums[r]==1:
                r+=1
                
            elif nums[r+1]-nums[r] > 1:
                l=r+1
                r=l  

            size= max(size,r-l+1)     
             

             

               
        
        return size

            
                
         
                      

        