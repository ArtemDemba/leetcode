# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()
        temp = head

        while temp:
            if temp in nodes:
                return True
            nodes.add(temp)
            temp = temp.next
        return False


if __name__ == '__main__':
    sol = Solution()
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = None
    # node4.next = node2
    print(sol.hasCycle(head))
