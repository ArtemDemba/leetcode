"""https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for index, item in enumerate(nums):
            if left_sum == total - left_sum - item:
                return index
            left_sum += item
        return -1

s = Solution()
test = [1,7,3,6,5,6]
print(s.pivotIndex(test))