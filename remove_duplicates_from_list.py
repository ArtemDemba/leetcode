"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d = {}
        index = 0
        total = 0
        while index != len(nums):
            if nums[index] not in d:
                d[nums[index]] = True
            else:
                total -= 1
            total += 1
            index += 1
        return total


s = Solution()
test = [1, 1, 2]
print(s.removeDuplicates(test))
print(test)