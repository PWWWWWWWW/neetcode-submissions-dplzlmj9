class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for val in s:
            s_dict[val] += 1

        for val in t:
            if val not in s_dict:
                return False
            s_dict[val] -= 1
        
        for freq in s_dict.values():
            if freq != 0:
                return False
        
        return True
