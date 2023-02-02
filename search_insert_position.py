"""https://leetcode.com/problems/search-insert-position/"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


test = [1, 2, 3, 4, 5]
print(Solution().searchInsert(test, 10))