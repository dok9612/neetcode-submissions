class Solution:
    def isValid(self, s: str) -> bool:
        #([])
        #({)} <- 
        if len(s)%2 != 0:
            return False

        bracket_map = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in bracket_map:
                last_bracket = stack.pop() if stack else '#'
                if last_bracket != bracket_map[char]:
                    return False
            else:
                stack.append(char)

        return not stack
