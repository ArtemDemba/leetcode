"""https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i"""
import sys
from time import time


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = int(-1 * sys.maxsize)
        curr = 0
        for x in nums:
            curr += x
            maxi = max(curr, maxi)
            if curr < 0:
                curr = 0
        return maxi


s = Solution()
test = [-2,1,-3,4,-1,2,1,-5,4]
start = time()
print(s.maxSubArray(test))
print(time() - start)
