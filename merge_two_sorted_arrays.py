"""https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i"""


from bisect import insort


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = nums1[:m]
        for inserted_item in nums2[:n]:
            insort(nums1, inserted_item)


s = Solution()
test1 = [1, 2, 3, 0, 0, 0]
test2 = [4, 0, 1, 0]
s.merge(test1, 3, test2, 4)
print(test1)
