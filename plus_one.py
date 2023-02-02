class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            indx = -1
            try:
                while digits[indx] == 9:
                    digits[indx] = 0
                    indx -= 1
                digits[indx] += 1
            except IndexError:
                digits[indx + 1] += 1
                digits.append(0)
            return digits
        digits[-1] += 1
        return digits


test = [9, 9, 9]
res = Solution().plusOne(test)
print(res)
