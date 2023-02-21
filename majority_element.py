"""https://leetcode.com/problems/majority-element/"""


from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = Counter(nums)
        for i in c.keys():
            if c[i] >= len(nums) / 2:
                return i


if __name__ == '__main__':
    s = Solution()
    test = [2,2,1,1,1,2,2]
    print(s.majorityElement(test))