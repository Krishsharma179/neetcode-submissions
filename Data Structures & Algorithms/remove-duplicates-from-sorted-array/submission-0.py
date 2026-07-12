class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first=0
        second=1

        while second <= len(nums)-1:
            if nums[first]==nums[second]:
                nums.remove(nums[first])
                
                
            else:
                first+=1
                second+=1


        return len(nums)            
