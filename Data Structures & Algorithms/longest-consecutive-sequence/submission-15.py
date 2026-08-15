class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # This will remove the duplicate terms

        nums = sorted(set(nums))
        longest_length = 1
        longest=1
        print(nums)
        if len(nums) == 0 :
            return 0

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                longest+=1
            else:
                longest = 1 
            longest_length=max(longest,longest_length)    
            
  

        return longest_length    


        
        


            
                
         
                      

        