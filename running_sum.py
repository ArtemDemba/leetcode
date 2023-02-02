"""https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(sum(nums[:i + 1]))
        return result


s = Solution()
test = [3,1,2,10,1]
print(s.runningSum(test))
