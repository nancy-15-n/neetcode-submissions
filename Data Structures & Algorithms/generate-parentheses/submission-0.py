from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if the string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add an opening bracket if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add a closing bracket if valid
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
