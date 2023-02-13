"""https://leetcode.com/problems/build-array-from-permutation/"""


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        return result


sol = Solution()
nums = [5,0,1,2,3,4]
print(sol.buildArray(nums))