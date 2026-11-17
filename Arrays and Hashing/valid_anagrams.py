# Valid Anagram (LeetCode 242)
# Approach: Two strings are anagrams exactly when every character appears the
#           same number of times in both, so compare their character counts.
# Time: O(n + m)  |  Space: O(k), where k is the number of distinct characters
#                   (O(1) for a fixed alphabet such as lowercase English letters)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
