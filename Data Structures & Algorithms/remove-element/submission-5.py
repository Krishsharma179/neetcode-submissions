class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # return the number of val which is not equal to val

        # we cannot change the size of the list while traversing over it val
        

        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]=nums[i]
                k+=1

        return k 







            


        


        
        
       