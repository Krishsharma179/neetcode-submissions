class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest=1

        # This solution has the better time complexity as compared to previous one 

        # before : I was sorting the hashset and after that i was maintaing a window with the longest sequesnce and returning the size 
        # After : In this since we dont sort the hashset we directly check if there is prev number in the set and increse the sixe if the my size +element is present in the set 
         

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

            
                
         
                      

        