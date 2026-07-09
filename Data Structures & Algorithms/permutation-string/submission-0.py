class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:n])

        if s1_count == window_count:
            return True

        for i in range(n, m):
            window_count[s2[i]] += 1
            window_count[s2[i-n]] -= 1
            if window_count[s2[i-n]] == 0:
                del window_count[s2[i-n]]
            if window_count == s1_count:
                return True

        return False


# Helper function to read input correctly
def read_input():
    s1 = "ab"
    s2 = "lecabee"
    return s1, s2