class Solution:
    def twoSum(self, nums: list, target):
        hashmap = {}

        for i, value in enumerate(nums):
            if target - value not in hashmap:
                hashmap[value] = i
            else:
                return [hashmap[target - value], i]


s = Solution()
test = [3, 3]
print(s.twoSum(test, 6))