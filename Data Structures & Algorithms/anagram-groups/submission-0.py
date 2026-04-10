class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            if str(sorted(s)) not in group.keys():
                group[str(sorted(s))] = [s]
            else:
                group[str(sorted(s))].append(s)
        return list(group.values())
