"""https://leetcode.com/problems/palindrome-number/"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = str(x)
        return result == result[::-1]


q = Solution()
print(q.isPalindrome(122))