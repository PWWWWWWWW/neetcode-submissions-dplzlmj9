class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                    
                top_element = stack.pop()

                if mapping[char] != top_element:
                    return False
                else:
                    continue
            
            else:
                stack.append(char)

        return not stack









        # stack = []
        # mapping = {")" : "(", "}" : "{", "]" : "["}
        # for element in s:
        #     if element in mapping.keys():
        #         top_element = stack.pop() if stack else "#"

        #         if mapping[element] != top_element:
        #             return False
        #         else:
        #             continue
        #     else:
        #         stack.append(element)
        
        # return not stack
                    
        # open_to_close = {"(": ")", "{" : "}", "[" : "]"}
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if open_to_close[s[l]] == s[r]: 
        #         l += 1
        #         r -= 1
        #         continue
        #     else:
        #         return False
        # return True