class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        #11234 val 1 -> 23411 return 3
        #121 val 1 -> 211 return 2
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return left