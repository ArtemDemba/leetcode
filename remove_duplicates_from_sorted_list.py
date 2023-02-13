"""https://leetcode.com/problems/remove-duplicates-from-sorted-list/"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        current = head
        possible_next = head.next

        while possible_next:
            if possible_next.val != current.val:
                current.next = possible_next
                current = current.next
                try:
                    while possible_next.val == possible_next.next.val:
                        possible_next = possible_next.next
                    possible_next = possible_next.next
                except AttributeError:
                    current.next = None
                    return head
            else:
                possible_next = possible_next.next
        current.next = None
        return head


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3))))

    temp = sol.deleteDuplicates(head)
    while temp:
        print(temp.val)
        temp = temp.next
