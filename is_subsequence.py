"""https://leetcode.com/problems/is-subsequence/description/"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        d = {}
        for index, char in enumerate(t):
            try:
                if char in s[i:]:
                    i += 1
                    if char in d:
                        continue
                    d[char] = True
            except IndexError:
                return True
        return len(d) == len(s)


sol = Solution()
s = 'leeeeetcode'
t = "ylyeyeyeyeyeyeytycyoydyey"
print(sol.isSubsequence(s, t))