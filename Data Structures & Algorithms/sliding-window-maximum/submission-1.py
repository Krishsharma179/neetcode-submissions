class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k
        max_element=[]
        while r<=len(nums):        
            max_element.append(max(nums[l:r]))
            l+=1
            r+=1    

        return max_element          

        