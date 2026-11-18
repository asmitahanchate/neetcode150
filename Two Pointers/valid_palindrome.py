# Valid Palindrome (LeetCode 125) - Two Pointers
# Approach: Keep only alphanumeric characters, lowercased, then compare the
#           cleaned sequence with its reverse.
#           (Two-pointer alternative: move l and r inward, skipping
#           non-alphanumeric characters, comparing lowercase; O(1) space.)
# Time: O(n)  |  Space: O(n) for the cleaned copy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaned_string = "".join(s.split())
        # cleaned_string = [cg.lower() for cg in cleaned_string if cg.isalnum()]
        # return cleaned_string == cleaned_string[::-1]

        # time complexity - O(n)
        cleaned_string = "".join(s.split()) 
        cleaned_string = [char.lower() for char in cleaned_string if char.isalnum()]
        return cleaned_string == cleaned_string[::-1]
