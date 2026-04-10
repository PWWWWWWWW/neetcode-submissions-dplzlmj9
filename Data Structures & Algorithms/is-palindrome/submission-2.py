class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()

        i = 0
        while i < (len(clean_s)//2):
            if clean_s[i] == clean_s[len(clean_s) - i - 1]:
                i += 1
            else:
                return False
        return True