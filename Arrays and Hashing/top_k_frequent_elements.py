# Top K Frequent Elements (LeetCode 347) - Arrays & Hashing
# Approach: Count with Counter, sort the counts by frequency (descending), take the first k keys.
# Time: O(n log n)  |  Space: O(n)
# Source: my original solution from revisiting_leetcode/top_k_frequent_elements.py

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # Make a freq hashmap using Counter
        sorted_freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse = True)) # This syntax was a bit tricky since we needed a way to sort the freq array based on the values. Highest number of value
        result = list(sorted_freq.keys())[:k] #This syntax is also new using lambdas, creating a list that has top "k" values from the sorted freq dictionary
        return result

        # Time complexity - O(n) for counting the numbers by going through nums and building a dictionary
        # Sorting time compexity - O(nlogn) because of python using tim sort
        # Final time complexity to make the result is O(k) because it only went through k elements 
        # i.e., O(n + nlogn + k)
        # Space complexity in - O(n + k)
        # 
