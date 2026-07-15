class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        count = {}
        res=[]
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1     
        
        for key,val in count.items():
            res.append([val,key])

        return max(res)[1]    
            
