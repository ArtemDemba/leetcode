"""https://leetcode.com/problems/roman-to-integer/description/"""


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        res = s.replace('IV', ' 4 ').replace('IX', ' 9 ').replace('XL', ' 40 ').replace('XC', ' 90 ')
        res = res.replace('CD', ' 400 ').replace('CM', ' 900 ')
        for char in res:
            if char in d:
                res = res.replace(char, f' {d[char]} ')
        result = sum(map(int, res.split()))
        return result


s = Solution()
print(s.romanToInt('LVIII'))
