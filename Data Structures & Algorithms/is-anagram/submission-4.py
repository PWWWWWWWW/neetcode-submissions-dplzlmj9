class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t: return False 

        hash_map_s = self.cal_hash(s)
        
        for char in t:
            if char in hash_map_s:
                hash_map_s[char] -= 1
                continue
            return False
        
        for value in hash_map_s.values():
            if value != 0: 
                return False

        return True
        
    def cal_hash(self, input_s: str) -> dict:
        hash_map = defaultdict()

        for char in input_s:
            hash_map[char] = hash_map.get(char, 0) + 1

        return hash_map

