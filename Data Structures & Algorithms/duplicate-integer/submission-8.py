class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s=set()
        output = False

        for i in nums:
            if i in s:
                output = True
            else:
                s.add(i) 

        return output

        