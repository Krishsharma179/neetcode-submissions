class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        Stat=False
        seen=set()
        for num in nums:
            if num in seen:
                Stat=True
            else:
                seen.add(num)    
        return Stat           

        