class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_allcharacter = []

        for char in s:
            if char.isalnum():
                list_allcharacter.append(char.lower())

        s = "".join(list_allcharacter)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

