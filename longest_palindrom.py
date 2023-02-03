"""https://leetcode.com/problems/longest-palindrome/description/"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        is_odd = False
        total = 0
        for i in set(s):
            if s.count(i) % 2 == 1:
                if not is_odd:
                    is_odd = True
                    total += s.count(i)
                else:
                    total += s.count(i) - 1
            else:
                total += s.count(i)
        return total


s = Solution()
test = 'a'
print(s.longestPalindrome(test))