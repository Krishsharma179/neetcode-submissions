class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res=[]
        # calculate n/3
        n = len(nums)

        thre = n // 3 

        # build hashmap
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1    
        
        for key,value in freq.items():
            if value > thre:
                res.append(key)

        return res                