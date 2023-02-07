"""https://leetcode.com/problems/climbing-stairs/description/"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        first, second = 1, 2
        for i in range(n - 1):
            first, second = second, first + second
        return first


s = Solution()
print(s.climbStairs(44))