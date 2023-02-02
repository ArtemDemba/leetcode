"""https://leetcode.com/problems/powx-n/description/"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = start_value = x
        if n < 0:
            res = start_value = 1 / x
        for _ in range(abs(n - 1 if n > 0 else n + 1)):
            res *= start_value
        return res


s = Solution()
print(s.myPow(2.4, 1))
