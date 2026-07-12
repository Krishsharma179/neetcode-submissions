class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This will be the dict that has the element has key and 
        # there frequency as value.

        count={}
        output=[]
        # This will have the key and the value will be 0

        for i in set(nums):
            count[i]=0

        for i in nums:
            count[i]= count[i] + 1
        
        new_counts=dict(sorted(count.items(), key=lambda item: item[1],reverse=True))
        
        for key in list(new_counts.keys())[:k]:
            output.append(key)
            

            

        return output        


            
        
        
            
              


        