class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # first we will initialize an count dict key will be the element          and value we be the frequency
        # [[3,3], [2,2] ,[1,1]]
        count={}
        arr=[]
        res=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

        for key,value in count.items():
            arr.append([value,key])


        arr.sort()

        for i in range(k):
            res.append(arr.pop()[1])


        return res    




                   

        
            



        
               


            
        
        
            
              


        