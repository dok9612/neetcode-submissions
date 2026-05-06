class Solution:
    # s = ({[]})
    def isValid(self, s:str) -> bool:
        if len(s) % 2 !=0:
            return False
        pmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        
        for par in s:
            if par in pmap:
                last_par = stack.pop() if stack else '#'
                if last_par != pmap[par]:
                    return False
            else:
                stack.append(par)
        return not stack