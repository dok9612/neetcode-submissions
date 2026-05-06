class Solution:
    def calPoints(self, operations:List[str]):
        nums = []
        for op in operations:
            if op == '+':
                nums.append(nums[-1] + nums[-2])
            elif op == 'D':
                nums.append(2*nums[-1])
            elif op == 'C':
                nums.pop()
            else:
                nums.append(int(op))
        return sum(nums)
        