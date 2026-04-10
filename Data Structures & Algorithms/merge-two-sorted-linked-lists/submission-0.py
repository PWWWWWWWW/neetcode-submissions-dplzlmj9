# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        
        if list2:
            tail.next = list2
        
        return dummy.next
        # prev_list1, curr_list1 = None, list1
        # prev_list2, curr_list2 = None, list2

        # while curr_list1 and curr_list2:

        #     if curr_list1.val <= curr_list2.val and curr_list1 == list1:
        #         head = list1
        #     elif curr_list1.val <= curr_list2.val:
        #         nxt1 = curr_list1.next
        #         curr_list1.next = curr_list2
        #         curr_list1 = nxt1
        #     elif curr_list1.val > curr_list2.val and curr_list2 == list2:
        #         head = list2
        #     else:
        #         nxt2 = curr_list2.next
        #         curr_list2.next = curr_list1
        #         curr_list2 = nxt2

        # return head


