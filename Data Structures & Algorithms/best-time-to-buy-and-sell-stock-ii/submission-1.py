class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        L = 0
        R = 0

        while L < len(prices)-1 and R < len(prices)-1:

            R += 1 


            if prices[R] - prices[L] > 0:
                profit += prices[R] - prices[L]
                L+=1
            else :
                L+=1    

        

        return profit         
        