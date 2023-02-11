"""https://leetcode.com/problems/backspace-string-compare/?envType=study-plan&id=level-1"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = list()
        stack_2 = list()

        for i in s:
            if i != '#':
                stack_1.append(i)
            else:
                try:
                    stack_1.pop(-1)
                except IndexError:
                    pass
        for i in t:
            if i != '#':
                stack_2.append(i)
            else:
                try:
                    stack_2.pop(-1)
                except IndexError:
                    pass

        return stack_1 == stack_2


sol = Solution()
s = 'a#c'
t = 'b'
print(sol.backspaceCompare(s, t))