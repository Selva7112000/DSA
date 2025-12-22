1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        # pair_index = {}
4        # for i, num in enumerate(nums):
5        #     pair_index[num] = i
6        #     newNum = target - num
7        #     if newNum in pair_index and pair_index[newNum] != i:
8        #         return [pair_index[newNum], i]
9        # return []
10
11        # pair_index = {}
12        # for i, num in enumerate(nums):
13        #     data_value = target - num
14        #     if data_value in pair_index:
15        #         return [pair_index[data_value], i]
16        #     pair_index[num] = i  
17        # return []
18
19
20        # data = {}
21        # for k, v in enumerate(nums):
22        #     value = target - v
23        #     if value in data:
24        #         return [data[value], k]
25        #     data[v] = k
26        # return []
27
28
29        # data = {}
30        # for k,v in enumerate(nums):
31        #     kav = target - v
32        #     if kav in data:
33        #         return [data[kav], k]
34        #     data[v] = k
35        # return []
36        data = {}
37        for k, v in enumerate(nums):
38            kv = target - v
39            if kv in data:
40                return [data[kv], k]
41            data[v] = k
42        return []
43
44
45
46        # nums.sort()
47        # left, right = 0, len(nums) - 1
48        # while left < right:
49        #     if nums[left] + nums[right] == target:
50        #         return [left, right]
51        #     elif nums[left] + nums[right] < target:
52        #         left += 1
53        #     else:
54        #         right -=1
55        # return []
56
57
58
59
60
61
62
63            
64            
65        