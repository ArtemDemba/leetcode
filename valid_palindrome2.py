"""https://leetcode.com/problems/valid-palindrome-ii/description/"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        first, second = 0, len(s) - 1

        while first <= second:
            if s[first] == s[second]:
                first += 1
                second -= 1
            else:
                test_s1 = s[:first] + s[first + 1:]
                test_s2 = s[:second] + s[second + 1:]

                return test_s1 == test_s1[::-1] or test_s2 == test_s2[::-1]
        return True


if __name__ == '__main__':
    sol = Solution()
    s = 'abc'
    print(sol.validPalindrome(s))

"""
e e
b b
c c
b b
b b
e e
e e
c c
a a
b b
b b
"""