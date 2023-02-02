"""https://leetcode.com/problems/longest-common-prefix/description/"""


import re


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = ''
        is_prefix = True
        i = 0
        current_prefix = ''

        while i < len(strs[0]):
            current_prefix += strs[0][i]
            for word in strs[1:]:
                if current_prefix not in word:
                    is_prefix = False
                    current_prefix = ''
                    break
            if is_prefix:
                longest = current_prefix
            i += 1
        return longest


s = Solution()
print(s.longestCommonPrefix(["c", "acc", "ccc"]))
