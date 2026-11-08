class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
          return 0
        left = 1
        right = x
        boundary = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid >= x:
                boundary = mid
                right = mid - 1
            else:
                left = mid + 1
        return boundary if boundary * boundary == x else boundary - 1