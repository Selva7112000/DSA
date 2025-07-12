class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_index = {}
        for i, num in enumerate(nums):
            newNum = target - num
            if newNum in pair_index:
                return [pair_index[newNum], i]
            pair_index[num] = i
            
        