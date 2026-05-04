class Solution:
    def removeElement(self, nums:List[int], val:int) -> List[int]:
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                # Overwrite the target with the last valid element in the current bounds
                nums[left] = nums[right - 1]
                # Shrink the valid array bound
                right -= 1
            else:
                # Element is valid, advance the checking pointer
                left += 1
                
        return left