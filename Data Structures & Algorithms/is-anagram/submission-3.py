class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        s_character_map = defaultdict(int)
        t_character_map = defaultdict(int)

        for char in s:
            s_character_map[char] += 1

        for char in t:
            t_character_map[char] += 1

        if s_character_map != t_character_map:
            return False

        return True
