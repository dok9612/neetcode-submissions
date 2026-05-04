# () [] ([])
# ([)] invalid

# stack | LIFO
# stack - accumulates, stacking it up.
# once close pop last stack and check if the paranthesis match
# if yes, keep this loop until empty -> true if not, false

from typing import List

class Solution:
	def isValid(self, s:str) -> bool:
		if len(s) % 2 != 0:
			return False
		stack:List = []
		h_map = {')':'(',']':'[','}':'{'}
		for char in s:
			if char in h_map:
				last_bracket = stack.pop() if stack else '#'
				if last_bracket != h_map[char]:
					return False
			else:
				stack.append(char)
		return not stack
