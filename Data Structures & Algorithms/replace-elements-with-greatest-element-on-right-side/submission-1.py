class Solution:
    def replaceElements(self, arr:List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            return [-1]
        
        max_val = -1
        for i in range(n-1, -1, -1):
            curr_val = arr[i]
            arr[i] = max_val
            if curr_val > max_val:
                max_val = curr_val
        return arr