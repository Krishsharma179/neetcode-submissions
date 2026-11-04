class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # state will be the sum of the array 

        #  invalid window will be 


        win_sum = 0
        L = 0
        R = 0
        min_len = len(nums)


        while L < len(nums) and R < len(nums):
             
            win_sum += nums[R]

            if R-L+1 == len(nums) and win_sum < target:
                return 0

            while win_sum >= target:
                min_len = min(min_len,R-L+1)
                win_sum -= nums[L]
                L += 1

            R +=1

        return min_len        

        