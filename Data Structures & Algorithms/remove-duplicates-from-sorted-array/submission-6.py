class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index = 0

        # 1234
        for read_index in range(len(nums)):
            if nums[read_index] != nums[write_index]:
                write_index += 1

                if read_index != write_index:
                    nums[write_index] = nums[read_index]
        return write_index + 1