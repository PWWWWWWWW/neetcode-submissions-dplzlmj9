"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pseudo
        # deep copy, new onject in heap and a new pointer in stack

        # hash table to store the origin one: new val
        # 找order，因為next的記憶體位置還沒被創建，所以在知道前一個位置指向一個maybe value = 3的地方時，再create 一個space which val = 3，next point to &新位置
        # random 邏輯相同，因為random的記憶體位置還可能沒被創建，所以在知道前一個位置指向一個maybe value = 3的地方時，再create 一個space which val = 3，random point to &新位置
        # hash_map = defaultdict()
        # curr = head
        # nxt_new = None
        # rand_new = None
        
        # while curr:
        #     hash_map[curr] = [curr.val, nxt_new, rand_new]

        # # 找order
        # for key, value in hash_map.items():
        #     for 
        #         if key.next.val == 
        # copy_random = ListNode()
        if not head:
            return None

        hash_map = defaultdict()
        curr = head

        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = hash_map[curr]
            copy.next = hash_map.get(curr.next)
            copy.random = hash_map.get(curr.random)
            curr = curr.next

        return hash_map[head]
