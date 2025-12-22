1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False 
5        data = {}
6        for i in s:
7            data[i] = data.get(i, 0) + 1
8        for j in t:
9            if j not in data:
10                return False
11            data[j] -= 1
12            if data[j] < 0:
13                return False
14        return True
15
16        