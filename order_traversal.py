"""https://leetcode.com/problems/binary-tree-level-order-traversal/description/"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_lvl = [root, ]
        result = [[root.val], ]

        while True:
            temp_list = []
            if not current_lvl:
                break
            for node in current_lvl:
                print(node.val, end=', ')
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            current_lvl = temp_list
            result.append([node.val for node in current_lvl])
        result.pop()
        return result


s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.levelOrder(root))
