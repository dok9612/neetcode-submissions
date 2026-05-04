class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        stack: list[str]= []
        hash_map: dict[str:str] = {')':'(',']':'[','}':'{'}

        for char in s:
            if char in hash_map:
                top_layer = stack.pop() if stack else '#'
                if hash_map[char] != top_layer:
                    return False
            
            else:
                stack.append(char)
        return not stack