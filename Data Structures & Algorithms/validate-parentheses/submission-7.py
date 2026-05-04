class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in hash_map:
                last_bracket = stack.pop() if stack else '#'
                if last_bracket != hash_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack