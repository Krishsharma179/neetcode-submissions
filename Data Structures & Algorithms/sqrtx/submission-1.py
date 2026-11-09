class Solution:
    def mySqrt(self, x: int) -> int:
        L = 1
        R = x 

        bound = -1

        if x ==0:
            return 0

        while L <= R:
            
            mid = (L + R) // 2

            if mid * mid >= x:
                bound = mid
                R = mid - 1 
            else:
                L = mid + 1 

        return bound  if bound*bound == x else bound -1            





        