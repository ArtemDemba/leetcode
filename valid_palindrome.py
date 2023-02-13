"""https://leetcode.com/problems/valid-palindrome/"""


from string import punctuation


class Solution:
    def isPalindrome(self, s: str) -> bool:
        for p in punctuation:
            s = s.replace(p, '')
        s = s.lower()
        s = s.replace(' ', '')
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()
    s = " "
    print(sol.isPalindrome(s))
