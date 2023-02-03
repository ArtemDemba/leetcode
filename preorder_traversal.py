"""https://leetcode.com/problems/n-ary-tree-preorder-traversal/?envType=study-plan&id=level-1"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list[int]:
        if not root:
            return []
        result = [root.val, ]

        def inner(node: Node):
            if node.children:
                for child in node.children:
                    result.append(child.val)
                    inner(child)

        inner(root)
        return result


s = Solution()
head = Node(val=1, children=[Node(val=3, children=[Node(5), Node(6)]), Node(2), Node(4)])
print(s.preorder(head))
