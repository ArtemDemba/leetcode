"""https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for index in range(len(s)):
            if s[index] not in d:
                if t[index] in d.values():
                    return False
                d[s[index]] = t[index]
            else:
                if d[s[index]] != t[index]:
                    return False
        return True


sol = Solution()
s = 'badc'
t = 'baba'
print(sol.isIsomorphic(s, t))