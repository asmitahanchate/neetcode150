# Sliding Window Maximum (LeetCode 239) - Sliding window (fixed size) + monotonic deque
# Approach: Keep a deque of candidate values in decreasing order (front = max).
#           When a new number arrives, pop smaller numbers off the back: they
#           can never be a window max again. When the window is full, the front
#           is the answer; if the front is the number leaving the window
#           (q[0] == nums[left]), pop it from the front.
#           Key fix: check q[0] == nums[left], not `nums[left] in q`
#           (popleft always removes the FRONT, and `in` is O(k)).
# Time: O(n) - each number is appended once and popped at most once
# Space: O(k) for the deque (plus O(n) for the output)
#
# Earlier attempts (kept below as comments): max(window) and heapify_max are
# O(n * k) and time out; a single running max can't forget numbers that left.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # left = 0
        # window = []
        # result = []
        # for right in range(len(nums)):
        #     window.append(nums[right])
        #     if (right-left+1) == k:
        #         max_win = max(window)
        #         result.append(max_win)
        #         window.remove(nums[left])
        #         left += 1
        # return result
        
        # Using heaps I thought it would be better time complexity
        # left =0
        # window, result = [],[]
        # for right in range(len(nums)):
        #     window.append(nums[right])
        #     if (right-left+1) == k:
        #         heapq.heapify_max(window)
        #         result.append(window[0])  
        #         window.remove(nums[left])
        #         left += 1
        # return result

        #Actual solution passing all test cases uses deque

        # Is not good for cases like[1,-1] and k = 1 coz answer is [1,-1] currMax stays positive
        # left = 0
        # result = []
        # currMax,actualMax = 0,0
        # for right in range(len(nums)):
        #     currMax = max(currMax, nums[right])
        #     if (right-left+1) == k:
        #         actualMax = max(actualMax,currMax)
        #         result.append(actualMax)
        #         left += 1
        # return result

        q = deque()
        left = 0
        result = []

        for right in range(len(nums)):
            while q and q[-1] < nums[right]:
                q.pop()
            q.append(nums[right])

            if right - left + 1 == k:
                result.append(q[0])
                if q[0] == nums[left]:
                    q.popleft()
                left += 1
        return result
