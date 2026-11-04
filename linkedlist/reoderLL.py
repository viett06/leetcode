# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # 1. Tìm node cuối của nửa đầu
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Tách thành hai danh sách
        second = slow.next
        slow.next = None

        # 2. Đảo ngược nửa sau
        prev = None
        current = second

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # 3. Nối xen kẽ hai nửa
        first = head
        second = prev

        while second is not None:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second
        
