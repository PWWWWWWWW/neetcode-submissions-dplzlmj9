class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        dup_set = set()

        for right in range(len(s)):
            while s[right] in dup_set:
                dup_set.remove(s[left])
                left += 1
            
            dup_set.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length

            
