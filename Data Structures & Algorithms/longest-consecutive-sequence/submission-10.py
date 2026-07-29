class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest=1

        

        if len(nums)==0:
            return 0


        nums_set=set(nums)     
        
        for i in nums_set:
            size=0
            if i-1 not in nums_set:
                size+=1

            while i+size in nums_set:
                size+=1

            longest=max(longest,size)

        return longest    

            
                
         
                      

        