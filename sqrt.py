"""https://leetcode.com/problems/sqrtx/"""


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while x // i >= i:
            i += 1
        return i - 1


s = Solution()
print(s.mySqrt(30))