"""https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        result = TreeNode(nums[mid])
        result.left = self.sortedArrayToBST(nums[:mid])

        result.right = self.sortedArrayToBST(nums[mid+1:])

        return result

