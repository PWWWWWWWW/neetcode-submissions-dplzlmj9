class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Pseudo code
        # iterate
        """
        iterate through s,
        hash table to store elements in the box and constantly renew max length,
        if the elements other than the biggest one count > k,
        move left pointer
        """
        left = 0
        hash_substring = defaultdict(int)
        max_len_substring = 0
        max_hash_substring = 0
        max_length = 0

        for right in range(len(s)):
            max_len_substring = right - left + 1
            hash_substring[s[right]] += 1
            max_hash_substring = max(max_hash_substring, hash_substring[s[right]])

            while max_len_substring - max_hash_substring > k:
                hash_substring[s[left]] -= 1
                left += 1
                max_len_substring = right - left + 1

            max_length = max(max_length, right - left + 1)

        return max_length
























        # if less frequntly appears more than k+1 elements, 
        # left pointer move to the position of less frequency one
        # left = 0
        # freq_characters = defaultdict(int)
        # max_length = 0
        # max_freq = 0

        # for right in range(len(s)):
        #     freq_characters[s[right]] += 1
        #     max_freq = max(freq_characters.values())

        #     while right - left + 1 - max_freq > k:
        #         freq_characters[s[left]] -= 1
        #         left += 1

        #     max_length = max(max_length, right - left + 1)

        # return max_length

        # 2 wrong sol
        # for right in range(len(s)):

        #     if s[right] not in freq_characters:
        #         freq_characters[s[right]] = 1
        #     else:
        #         freq_characters[s[right]] += 1

        #     if sum(freq_characters.values()) - max(freq_characters.values()) > k:
        #         current_length = right - left
        #         max_length = max(max_length, current_length)

        #         while s[left] ==  max(freq_characters.values()):
        #             left += 1
        #             freq_characters[s[left]] -= 1

        #         left += 1
        #         freq_characters[s[left]] -= 1
            
        #     else:
        #         current_length = right - left + 1
        #         max_length = max(max_length, current_length)

        # return max_length 

            # if s[right] not in freq_two_characters and len(distinct_characters)  and 

            # if s[right] not in distinct_characters and len(distinct_characters) > 1 and dup >= 0:
            #     dup -= 1
            #     right += 1

            #     current_length = right - left + 1
            #     max_length = max(max_length, current_length)
            #     left += 1