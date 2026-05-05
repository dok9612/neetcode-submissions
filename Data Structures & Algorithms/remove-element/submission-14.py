class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        #12345 val 1 -> 23451
        #1123 val 1 -> 2311
        #123 val 4 ->
        if not nums:
            return 0
        write_pointer = 0
        for read_pointer in range(len(nums)):
            if nums[read_pointer] != val:
                if read_pointer != write_pointer:
                    nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        return write_pointer
