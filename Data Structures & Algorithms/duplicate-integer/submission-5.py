class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate=False
        new_nums=sorted(nums)
        for i in range(len(new_nums)-1):
            if new_nums[i]==new_nums[i+1]:
                duplicate=True
           
        return duplicate    




        
        