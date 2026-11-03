class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0 
        R = 0
        state = 0  

        while L < len(prices)-1 and R < len(prices)-1:
            R += 1
            
            state = max(state , prices[R] - prices[L])

            while prices[R] - prices[L] < 0:
                L += 1
        return state
            
                

        