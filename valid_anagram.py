"""https://leetcode.com/problems/valid-anagram/?envType=study-plan&id=data-structure-i"""


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2


sol = Solution()
s = 'rat'
t = 'car'
print(sol.isAnagram(s, t))