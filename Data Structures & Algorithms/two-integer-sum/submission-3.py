class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # dictionary to store value:index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # return smaller index first
                return [seen[complement], i] if seen[complement] < i else [i, seen[complement]]
            seen[num] = i
