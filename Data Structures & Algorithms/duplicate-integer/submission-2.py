class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Status=False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                Status=True
            

        return Status            

        