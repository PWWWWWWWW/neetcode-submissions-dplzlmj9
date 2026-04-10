# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        if not head or not head.next:
            return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

        # slow, fast = head, head

        # while slow != fast:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if not fast:
        #         return False

        # return True

        # visited = set()
        # curr = head

        # while curr:
        #     if curr in visited:
        #         return True
            
        #     visited.add(curr)
        #     curr = curr.next

        # return False