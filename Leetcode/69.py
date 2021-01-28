class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = int(x / 2)

        while start <= end:
            mid = int((start + end) / 2)
            if x < mid:
                end = mid - 1
            elif x > mid:
                start = mid + 1
            else:
                return mid

        return start - 1
sol = Solution()
sol.mySqrt(8)