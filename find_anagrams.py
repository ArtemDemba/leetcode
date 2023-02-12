"""https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=study-plan&id=level-1"""


from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        counter_p = Counter(p)
        result = []

        for i in range(len(s) - len(p) + 1):
            counter_s = Counter(s[i:i + len(p)])
            if counter_s == counter_p:
                result.append(i)

        return result


if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    sol = Solution()
    print(sol.findAnagrams(s, p))
