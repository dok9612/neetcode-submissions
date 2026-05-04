from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        max_num = -1
        for i in range(len(arr)-1, -1, -1):
            curr_num = arr[i]
            arr[i] = max_num

            if curr_num > max_num:
                max_num = curr_num
        return arr