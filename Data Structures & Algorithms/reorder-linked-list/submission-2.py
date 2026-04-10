# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # pseudo code
        # seperate into two linked list
            # fast two step vs slow one step (turtle rabbit racing)
        # reverse the second half
        # merge two linked list
            # iterate
            # fill in inorder

        # seperate into two linked list
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reverse = slow.next
        slow.next = None

        # reverse
        prev = None
        curr = reverse

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merged
        # 2永遠比1等於或更短，所以\
        first, second = head, prev

        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2