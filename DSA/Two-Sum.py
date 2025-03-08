class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # data = {}
        # for i in range(len(nums)):
        #     data[nums[i]] = i

        # for i,num in enumerate(nums):
        #     data1 = target - num
        #     if data1 in data and data[data1] != i:
        #         return i,data[data1]

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+ nums[j] == target:
        #             return [i,j]

        data = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            newN = target - nums[i]
            if newN in data and i != data[newN]:
                return i,data[newN]
        # l,r = 0,len(nums) - 1
        # while l < r:
        #     if nums[l] + nums[r] == target:
        #         return [l,r]
        #     elif nums[l] + nums[r] > target:
        #         r-=1
        #     else:
        #         l+=1
                
            

        
            



        