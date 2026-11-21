# Encode and Decode Strings (LeetCode 271) - Arrays & Hashing
# Approach: Encode each string as len + '#' + string. To decode, read digits up to '#',
#           then take exactly that many characters, so '#' inside a string is safe.
# Time: O(n)  |  Space: O(n) for the output
# Source: my original solution from revisiting_leetcode/encode_decode_string.py

# You basically need a way to delimit so that even if you have a symbok in your string, you don't count it as the delimiter
class Solution:

    def encode(self, strs: List[str]) -> str:
        # How do you know what is the delimiter, it can be any sign
        # Put the len of the str followed by a delimiter so you check how many chars you have to go through
        # Till you hit the delimter
        # E.g., "4#neet" means 4 chars until delimter and then read 4 chars whatever comes after delimiter
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result


    def decode(self, s: str) -> List[str]:
        result, pos = [], 0 #position of the number
        while pos < len(s): 
            # Go up till the len of each string e.g., "4#neet" where pos=0 i.e., 4
            j = pos
            while s[j] != "#": # Go up till the delimiter
                j +=1 # Now j = 1 because that is where our # is
            length = int(s[pos:j]) # i.e., int(str[0:1]) i.e., 4
            pos = j + 1   # To go to the next word
            j = pos + length
            result.append(s[pos:j]) # appned(str[2:6]) i.e., neet
            pos = j
        return result

# Time complexity - O(n) going through the string once
# Space complexity - O(1). In leetcode storage doesn't count for extra lists otherwise O(n) for storing result
