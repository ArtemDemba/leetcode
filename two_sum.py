class Solution:
    def twoSum(self, nums: list, target):
        values = {}

        for indx in range(len(nums)):
            temp = target - nums[indx]
            if temp in values:
                return [indx, values[temp]]
            values[nums[indx]] = indx


s = Solution()
test = [2,7,11,15]
print(s.twoSum(test, 9))