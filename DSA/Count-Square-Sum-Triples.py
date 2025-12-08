1class Solution:
2    def countTriples(self, n: int) -> int:
3        sq = {i*i for i in range(1, n+1)}
4        r = 0
5
6        for i in range(1, n+1):
7            temp = i*i
8            for j in range(i*1, n+1):
9                s = temp + j*j
10
11                if s in sq:
12                    r+= 2
13        return r
14        
15        