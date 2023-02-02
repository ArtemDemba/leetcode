"""https://leetcode.com/problems/remove-element/"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

s = Solution()
test = [1,2,3,4,1,2,3]
s.removeElement(test, 2)
print(test)
