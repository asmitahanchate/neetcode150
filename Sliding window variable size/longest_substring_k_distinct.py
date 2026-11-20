# Longest Substring with At Most K Distinct Characters (LeetCode 340, Premium)
# - Sliding window (variable size)
# Approach: Count characters in the window with a dict. Add s[right] first;
#           while the window has more than k distinct characters, shrink from
#           the left, deleting a character when its count hits 0 (otherwise
#           len(unique) never drops). The window is valid after the while, so
#           update maxLength there.
#           Pattern: add right -> while invalid, shrink left -> measure.
# Time: O(n)  |  Space: O(k)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Lets keep a window set to note down any seen chars

        # At most k means <=k keep going
        # Lets also keep a length and a maxLength and return maxLength
        left, length,maxLength = 0,0,0
        # Use a dict and not a set to keep comparing the count
        unique = {}

        for right in range(len(s)):
            unique[s[right]] = 1 + unique.get(s[right],0)
            #If there are k unique characters in the map with whataver counts
            while len(unique) > k:
                #Start removing left 
                unique[s[left]] -= 1
                if unique[s[left]] == 0:
                    del unique[s[left]]
                left += 1
            length = right - left + 1
            maxLength = max(maxLength, length)
        return maxLength
