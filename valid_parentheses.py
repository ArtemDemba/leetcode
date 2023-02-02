"""https://leetcode.com/problems/valid-parentheses/"""


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        res = s

        while res:
            if '()' in res or '[]' in res or '{}' in res:
                res = res.replace('()', '').replace('[]', '').replace('{}', '')
            else:
                return False
        return True


s = Solution()
print(s.isValid('(){}}{'))




