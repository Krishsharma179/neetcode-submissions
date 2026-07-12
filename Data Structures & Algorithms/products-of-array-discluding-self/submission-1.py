class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        
        #[1,2,4,6]

        product=1
        
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                if i != j:
                    product=product*nums[j]
                
            output.append(product)
            product=1
      

        return output   
            
        