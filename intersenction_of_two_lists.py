"""https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=study-plan&id=data-structure-i"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        intersection_set = set1 & set2
        result = []
        for item in intersection_set:
            count = nums1.count(item) if nums1.count(item) < nums2.count(item) else nums2.count(item)
            result += [item] * count
        return result


s = Solution()
test1 = [1, 2, 2, 1]
test2 = [2, 2]
s.intersect(test1, test2)