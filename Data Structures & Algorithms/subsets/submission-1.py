from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # Add current subset
            res.append(path[:])
            
            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(0, [])
        return res
