class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 1112345 -> 12345... return 4
        # 1234 -> 1234 return 4
        write_index = 0
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[write_index]:
                write_index += 1
                
                if read_index != write_index:
                    nums[write_index] = nums[read_index]
        return write_index + 1
