class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        #stack LIFO
        hashmap = {')':'(',']':'[','}':'{'}
        stack = []

        for char in s:
            if char in hashmap:
                # this is a closing bracket
                last_bracket = stack.pop() if stack else '#'
                if hashmap[char] != last_bracket:
                    return False
            else:
                # this is an opening bracket
                stack.append(char)
        return not stack