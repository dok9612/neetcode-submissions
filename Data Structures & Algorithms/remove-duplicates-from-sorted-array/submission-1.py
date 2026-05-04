from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'write_index' tracks the tail of the valid, unique array.
        # It represents the last confirmed unique element.
        write_index = 0 
        
        # 'read_index' scans the array to find new candidates.
        for read_index in range(1, len(nums)):
            
            # Generative Concept: Exploiting Sorted Property
            # We only care if the stream changes value.
            if nums[read_index] != nums[write_index]:
                
                write_index += 1
                
                # Senior Optimization: Avoid Self-Assignment
                # Only write to memory if the indices actually differ.
                # This reduces bus traffic in massive data processing.
                if write_index != read_index:
                    nums[write_index] = nums[read_index]
        
        # Return length (index + 1)
        return write_index + 1