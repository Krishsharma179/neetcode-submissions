class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This will be the dict that has the element has key and 
        # there frequency as value.
        
        '''
        {
        7:2
        3:1
        1:1
        }
        ''' 
        
        count={}
        res=[]
        arr=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1

       
        
        for key,val in count.items():
            arr.append([val,key])

        arr.sort()

        for i in range(k):
            res.append(arr.pop()[1])



        return res         
            

            



        
               


            
        
        
            
              


        