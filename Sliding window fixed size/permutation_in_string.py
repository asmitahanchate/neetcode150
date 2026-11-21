# Permutation in String (LeetCode 567) - Sliding Window
# Approach (as written): from each start i, extend j while no character count exceeds s1's;
#           when every character count matches, it's a permutation.
#           Worst case O(n * m); the fixed-size window version (slide a window of len(s1)
#           and compare counts) is O(n).
# Time: O(n * m) as written  |  Space: O(1) (at most 26 letters)
# Source: my original solution from revisiting_leetcode/permutation_string.py

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Won't work because does not preserve order
        # freq1 = Counter(s1)
        # freq2 = Counter(s2)

        # for char in s1:
        #     if freq1[char] == freq2[char]:
        #         return True
        #     else:
        #         return False
        
        # This was harder than I thought 

        count1 = Counter(s1)
        need = len(count1)
        for i in range(len(s2)): # i goes up till n so time complexity - O(n)
            count2, cur = {}, 0 
            for j in range(i, len(s2)): # j is just another pointer that traverses only 
            # once not at every iteration of i 
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                # count2[c] = 1 + count2.get(c) if count2.get(c) not 0
                # {'c': '1'} initially once we enounter 'c'
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                # If we have more than required 'c's in count2 then break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                # This is our case for test case 1 
                    cur += 1
                if cur == need:
                    return True
        return False
            






               
