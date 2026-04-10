# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
        
        # # reverse solution
        # # REVERSE
        # prev = None
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # # # DELETE
        # # delete = prev
        # # prev_delete = ListNode()
        # # next_delete = ListNode()

        # # while n > 0:
        # #     prev_delete = delete
        # #     next_delete = delete.next.next
        # #     delete = delete.next
        # #     n -= 1

        # # prev_delete.next = next_delete

        # # DELETE (刪除反轉後的第 n 個)
        # dummy = ListNode(0, prev)
        # curr = dummy
        # for _ in range(n - 1): 
        #     curr = curr.next

        # # 刪除第 n 個
        # curr.next = curr.next.next

        # # ⭐ 關鍵修正：重新獲取正確的頭部
        # # 因為原本的 prev 可能已經被刪除了，或者不再是頭部
        # new_head_to_reverse = dummy.next

        # # REVERSE BACK
        # curr = new_head_to_reverse
        # prev_back = None # 換個名字避免混淆

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev_back
        #     prev_back = curr
        #     curr = nxt

        # return prev_back