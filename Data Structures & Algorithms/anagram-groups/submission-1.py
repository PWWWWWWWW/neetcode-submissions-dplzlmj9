class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                num = ord(char) - ord("a")
                count[num] += 1
            if tuple(count) not in group.keys():
                group[tuple(count)] = [s]
            else:
                group[tuple(count)].append(s)
        return list(group.values())
        # group = {}
        # for s in strs:
        #     if str(sorted(s)) not in group.keys():
        #         group[str(sorted(s))] = [s]
        #     else:
        #         group[str(sorted(s))].append(s)
        # return list(group.values())
