"""https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return not len(set(nums)) == len(nums)


s = Solution()
test = [1,2,3,4, 1]
print(s.containsDuplicate(test))