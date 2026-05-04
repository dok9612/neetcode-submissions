class Solution:
    def removeElement(self, nums:List[int], val:int) -> List[int]:
        first_p = 0
        for second_p in range(len(nums)):
            if nums[second_p] != val:
                nums[first_p] = nums[second_p]
                first_p += 1
        return first_p