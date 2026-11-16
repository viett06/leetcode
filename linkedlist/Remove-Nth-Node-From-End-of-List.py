# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        for _ in range(n):
            right = right.next

        while right.next is not None:
            left = left.next
            right = right.next
        node_to_remove = left.next
        left.next = node_to_remove.next
        return dummy.next

