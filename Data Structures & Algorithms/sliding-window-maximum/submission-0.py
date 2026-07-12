class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        max_element=[]
        while r<=len(nums)-1:
            lst=[]
            for i in range(l,r+1):     
                lst.append(nums[i])

            max_element.append(max(lst))
            l+=1
            r+=1    
                

        return max_element          

        