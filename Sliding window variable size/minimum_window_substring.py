# Minimum Window Substring (LeetCode 76) - Sliding window (variable size)
# TODO: COME BACK TO THIS AND SOLVE IT AGAIN.
#
# Approach: need = Counter(t); count = how many chars of t are still missing
#           (starts at len(t)). Expand right: if need[c] > 0 it was useful, so
#           count -= 1; decrement need[c] for every char (extras go negative).
#           While count == 0 the window has everything: record it if it's the
#           shortest, give s[left] back (need += 1; if it goes > 0 we lost a
#           needed char, so count += 1), and move left.
#           Fixed from my first try: count started at 0, duplicates in t weren't
#           counted, the shrink loop checked s[right] instead of s[left], and
#           left only moved inside an if (infinite loop).
# Time: O(n + m)  |  Space: O(m)   (n = len(s), m = len(t))

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left, length, minLength = 0, 0, float("inf")
        count = len(t)          # CHANGED: count = how many chars of t are still missing
        start = 0               # ADDED: where the best window starts (to return it)

        for right in range(len(s)):
            if need[s[right]] > 0:      # CHANGED: this char was still needed
                count -= 1
            need[s[right]] -= 1         # CHANGED: decrement for EVERY char (extras go negative)

            while count == 0:           # CHANGED: shrink while the window has everything
                length = right - left + 1
                if length < minLength:  # ADDED: remember where the best window starts
                    minLength = length
                    start = left
                need[s[left]] += 1      # give s[left] back
                if need[s[left]] > 0:   # we just gave away a char we needed
                    count += 1
                left += 1               # CHANGED: always move left (it was inside the if)
        return "" if minLength == float("inf") else s[start:start + minLength]   # CHANGED: return the substring
