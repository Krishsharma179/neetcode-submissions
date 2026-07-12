class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
         
        k=k%len(nums)
        first=0
        last=len(nums)-1
        while first<last:
            temp=nums[last]
            nums[last]=nums[first]
            nums[first]=temp

            first+=1
            last-=1
        
        first=0
        last=k-1
        while first<last:
            
            temp=nums[last]
            nums[last]=nums[first]
            nums[first]=temp

            first+=1
            last-=1
        
        first=k
        last=len(nums)-1
        while first<last:
            
            temp=nums[last]
            nums[last]=nums[first]
            nums[first]=temp

            first+=1
            last-=1

          


            






            
        
        
        
        
        
        
        
            



            

            
            



    

    


        