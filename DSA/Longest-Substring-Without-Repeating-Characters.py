class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        data = {}
        for i, value in enumerate(s):
            if value in data and data[value] >= left:
                left = data[value] + 1
            max_length = max(max_length, i - left +1)
            data[value] = i
        return max_length
        
        