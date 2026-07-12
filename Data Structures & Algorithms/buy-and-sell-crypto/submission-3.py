class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=0
        profit = 0
        
        while s < len(prices)-1:

            if prices[b]>prices[s]:
                b+=s-b
                s+=1

            else:
                s+=1 

            print(prices[b],prices[s])       

            profit = max(profit , prices[s]-prices[b])    

        return profit     


        
       
                
            



        

                    

        
        