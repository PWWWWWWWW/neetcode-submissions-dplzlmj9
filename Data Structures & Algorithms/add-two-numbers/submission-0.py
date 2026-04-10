# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_node = v1 + v2 + carry
            remainder = sum_node % 10
            carry = sum_node // 10

            curr.next = ListNode(remainder)
            curr = curr.next
            
            if l1: 
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return dummy.next
        
        # pseudo
        '''
        reverse andget the true number, adding and create a new linked list
        '''
        # curr1 = l1
        # curr2 = l2
        # hash_map = defaultdict()

        # while curr1 and curr2:
        #     sum_val = curr1.val + curr2.val + sum_val_Quotient
        #     sum_val_remainder = sum_val % 10
        #     sum_val_Quotient = sum_val // 10
        #     sum_new = Node(sum_val_remainder)

        #     curr1 = curr1.next
        #     curr2 = curr2.next


    #     # 1. 定義一個反轉函數
    # def reverseList(self, head):
    #     prev, curr = None, head
    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev # 回傳新的頭 