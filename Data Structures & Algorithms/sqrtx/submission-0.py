class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            square_mid = mid * mid
            if square_mid == x:
                return mid
            elif square_mid < x:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans