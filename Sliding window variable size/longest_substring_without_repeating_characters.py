# Longest Substring Without Repeating Characters (LeetCode 3)
# - Sliding window (variable size)
# Approach: The window s[left..right] always holds unique characters, tracked
#           in a set. Before adding s[right], shrink from the left until
#           s[right] is no longer in the window, then add it and record the
#           window's length. Each character enters and leaves the set at most
#           once, so the inner while does O(n) work in total, not per step.
# Time: O(n)  |  Space: O(min(n, m)), m = size of the character set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # For duplicates try and use a set
        window = set()
        left, length = 0, 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            length = max(length, right - left + 1)
        return length
