class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False
        hash_count = {}
        for char in s:
            if char not in hash_count:
                hash_count[char] = 1
            else:
                hash_count[char] += 1
        
        for char in t:
            if char not in hash_count:
                return False
            hash_count[char] -= 1
        # if hash_count 裡有數字不是0的 return True
        for val in hash_count.values():
            if val !=0:
                return False
        return True
        
