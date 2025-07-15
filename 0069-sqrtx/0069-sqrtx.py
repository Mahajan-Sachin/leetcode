class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x < 0:
            return 0  # Optional: Python supports complex, but for int return 0

        start = 0
        end = x
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid == x:
                return mid  # ✅ Found perfect square, no need to continue
            elif mid * mid < x:
                ans = mid   # ✅ Floor value
                start = mid + 1
            else:
                end = mid - 1

        return ans
