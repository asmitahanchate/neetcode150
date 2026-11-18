# Valid Palindrome (LeetCode 125) - Two Pointers version
# Approach: Clean the string (alphanumeric only, lowercased), then walk
#           left and right pointers toward the middle; any mismatch means
#           it's not a palindrome.
# Time: O(n)  |  Space: O(n) for the cleaned copy
#       (O(1) space if the pointers skip non-alphanumerics on the original s)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(s.split()) 
        cleaned_string = [char.lower() for char in cleaned_string if char.isalnum()]
        left, right = 0, len(cleaned_string) - 1
        while left < right:
            if cleaned_string[left] != cleaned_string[right]:
                return False
            left += 1
            right -=1
        return True
