class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # pseudo
        # hash_map to store all the patterns
        # create built in anagram function
        # iterate through all of these 
        patterns = defaultdict(list)
        
        for s in strs:
            curr_pattern = tuple(self.string_pattern(s))
            patterns[curr_pattern].append(s)
        
        return list(patterns.values())


    def string_pattern(self, s: str) -> list:
        pattern = [0] * 26

        for char in s:
            distinct_char = ord(char) - ord('a') 
            pattern[distinct_char] += 1

        return pattern

    #     patterns = defaultdict(list)

    #     for s in strs:
    #         pattern = tuple(sorted(self.create_dict(s).items()))
    #         patterns[pattern].append(s)

    #     return list(patterns.values())


    # def create_dict(self, s: str) -> dict:
    #     hash_map = {}

    #     for char in s:
    #         hash_map[char] = hash_map.get(char, 0) + 1

    #     return hash_map