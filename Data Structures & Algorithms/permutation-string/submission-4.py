class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # len(s1) in s2 should contain permulation of s1
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length > s2_length:
            return False

        hash_map = defaultdict(int)
        s2_windows_map = defaultdict(int)

        for char in s1:
            hash_map[char] += 1
        
        for char in s2[:s1_length]:
            s2_windows_map[char] += 1

        # ⭐ 修正：先比對第一個視窗！
        if hash_map == s2_windows_map:
            return True

        for right in range(s1_length, s2_length):
            right_char = s2[right]
            s2_windows_map[right_char] += 1

            left_char = s2[right - s1_length]
            s2_windows_map[left_char] -= 1

            if s2_windows_map[left_char] == 0:
                del s2_windows_map[left_char]

            if hash_map == s2_windows_map:
                return True

        return False

        # for right in range(k - 1, len(s2), 1):
        #     left = right - k + 1

        #     if s2[right] not in hash_map:
        #         left = right + 1
        #     else:
        #         hash_map[s2[right]] -= 1

        #         for val in hash_map.values():
        #             if val != 0:
        #                 return False
            
        #     return True
