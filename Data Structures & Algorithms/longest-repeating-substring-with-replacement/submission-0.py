class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # dictionary to store frequency of characters
        left = 0
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # update frequency of current character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # check if window is valid
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update result
            result = max(result, right - left + 1)

        return result