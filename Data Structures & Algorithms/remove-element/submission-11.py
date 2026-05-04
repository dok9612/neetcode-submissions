class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        # 12345 1 23451
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return left