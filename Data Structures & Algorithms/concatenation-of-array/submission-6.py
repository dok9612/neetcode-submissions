class Solution:
    def getConcatenation(self, nums:List[int]) -> List[int]:
        if not nums:
            return []
        n:int = len(nums)
        ans:List[int] = [0]*2*n

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans