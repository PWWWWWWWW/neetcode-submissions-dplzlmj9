class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_map_s = self.create_hash_map(s)

        for char in t:
            if hash_map_s.get(char, 0) == 0:
                return False

            hash_map_s[char] -= 1

        return True


    def create_hash_map(self, s: str) -> dict:
        hash_map = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        return hash_map

    





















    #     len_s = len(s)
    #     len_t = len(t)

    #     if len_s != len_t: return False 

    #     hash_map_s = self.cal_hash(s)
        
    #     for char in t:
    #         if char in hash_map_s:
    #             hash_map_s[char] -= 1
    #             continue
    #         return False
        
    #     for value in hash_map_s.values():
    #         if value != 0: 
    #             return False

    #     return True
        
    # def cal_hash(self, input_s: str) -> dict:
    #     hash_map = defaultdict()

    #     for char in input_s:
    #         hash_map[char] = hash_map.get(char, 0) + 1

    #     return hash_map

