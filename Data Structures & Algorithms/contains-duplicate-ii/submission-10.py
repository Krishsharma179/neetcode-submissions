class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # what is the condition that says the window is valid ?

        # nums[j] == nums[i] and abs(i-j) <= k

        #According to me this is not a  sliding window problem because sliding window is mostly
        #based on subarray or the contigous element in the window 

        Hash = set()
        state = False
        L=0

        for i in range(len(nums)):
            if nums[i] in Hash and abs(L-i) > k:
                Hash.remove(nums[L])
                L+=1
            if nums[i] in Hash and abs(L- i) <=k:
                return True
                
            
            Hash.add(nums[i])
      
        return state
                


