class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_char = []

        for char in s:
            if char.isalnum():        
                filter_char.append(char.lower())
        
        new_s = ''.join(filter_char)

        left = 0
        right = len(new_s) - 1

        while left <= right:
            if new_s[left] != new_s[right]:
                return False

            left += 1
            right -= 1

        return True