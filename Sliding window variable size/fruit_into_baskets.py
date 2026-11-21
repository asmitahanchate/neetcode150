# Fruit Into Baskets (LeetCode 904) - Sliding window (variable size)
# Approach: Same as Longest Substring with At Most K Distinct Characters with
#           k = 2 (two baskets = at most 2 fruit types). Count fruit types in
#           the window; while there are more than 2 types, shrink from the left
#           and delete a type when its count hits 0. Measure after the while.
# Time: O(n)  |  Space: O(1) (the dict never holds more than 3 types)

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Similar to Longest substring with k unique characters
        # Here k == 2 because 2 distinct types of fruits so k = 2
        unique = {}
        left, length, maxLength = 0, 0, 0 

        for right in range(len(fruits)):
            unique[fruits[right]] = 1 + unique.get(fruits[right],0)
            while len(unique) > 2:
                unique[fruits[left]] -= 1
                if unique[fruits[left]] == 0:
                    del unique[fruits[left]]
                left += 1
            length = right - left + 1
            maxLength = max(maxLength, length)
        return maxLength
