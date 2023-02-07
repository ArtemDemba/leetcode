"""https://leetcode.com/problems/binary-search/"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


test = [-1,0,3,5,9,12]
s = Solution()
print(s.search(test, -2))