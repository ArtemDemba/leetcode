class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = 0
        indx = 1 - len(a)
        while indx != 1:
            result += (2 ** abs(indx) if a[indx - 1] == '1' else 0)
            indx += 1
        indx = 1 - len(b)
        while indx != 1:
            result += (2 ** abs(indx) if b[indx - 1] == '1' else 0)
            indx += 1

        return bin(result)[2:]


print(Solution().addBinary('1010', '1011'))

