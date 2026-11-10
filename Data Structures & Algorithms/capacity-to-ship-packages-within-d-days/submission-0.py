class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        L = max(weights)
        R = sum(weights)
        
        def ship(k):
            # This will return if the capacity is ok or not 
            ships,currcap=1,k
            
            for i in weights:
                if currcap-i< 0:
                    ships+=1
                    if ships > days:
                        return False 
                    currcap = k
                currcap -= i

            return True                    
                    

        bound = -1 

        while L <= R:

            mid = (L + R) // 2 

            if ship(mid) :
                bound = mid 
                R = mid - 1
            else:
                L = mid + 1  

        return bound             





        