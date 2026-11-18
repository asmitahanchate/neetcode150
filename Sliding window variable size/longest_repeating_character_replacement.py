# Longest Repeating Character Replacement (LeetCode 424)
# - Sliding window (variable size)
# Approach: Count the letters in the window s[left..right]. The characters
#           that must be replaced = window length - count of the most frequent
#           letter. If that exceeds k, the window is invalid, so slide left
#           forward by one. An `if` (not `while`) is enough: the window never
#           has to shrink below the best length found so far, it only slides.
# Time: O(26 * n) = O(n)  |  Space: O(1) (at most 26 keys in count)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        #Will have at most 26 values for 26 letters of an alphabet
        result, left = 0,0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            if (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right- left + 1)
        return result
