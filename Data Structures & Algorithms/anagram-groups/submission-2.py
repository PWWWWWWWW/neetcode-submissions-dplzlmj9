class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_hash_map = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagrams_hash_map[key].append(s)

        return list(anagrams_hash_map.values())
            