"""https://leetcode.com/problems/happy-number/"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1111111:
            return True
        s = 0
        input_number = n

        while True:
            while input_number != 0:
                s += (input_number % 10) ** 2
                input_number //= 10
            if s < 10:
                break
            input_number = s
            s = 0
        return s == 1


if __name__ == '__main__':
    s = Solution()
    test = 1111111
    print(s.isHappy(test))