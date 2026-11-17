# Group Anagrams (LeetCode 49)
# Approach: Anagrams share the same sorted string, so use ''.join(sorted(s))
#           as a dictionary key and append each word to its key's list.
#           The dictionary's values are the groups.
# Time: O(n * k log k)  |  Space: O(n * k)
#       (n = number of strings, k = length of the longest string)

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in master:
                master[key] = []
            master[key].append(s)
        return list(master.values())
