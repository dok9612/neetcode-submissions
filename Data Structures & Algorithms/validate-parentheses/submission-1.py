class Solution:
    def isValid(self, s: str) -> bool:
        #s = ()[[]]
        #([]) not ([)]
        if len(s)%2 != 0:
            return False
            
        stack = []
        hashmap = {']':'[','}':'{',')':'('}

        for char in s:
            if char in hashmap:
                # closing bracket
                last_bracket = stack.pop() if stack else '#'
                if last_bracket != hashmap[char]:
                    return False
            else:
                stack.append(char)
        return not stack

                