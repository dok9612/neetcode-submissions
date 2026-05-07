class Solution:
    def isValid(self,s:str) -> bool:
        stack = []
        par_dict = {']':'[','}':'{',')':'('}
        
        for char in s:
            if char in par_dict:
                last_par = stack.pop() if stack else '#'
                if last_par != par_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack