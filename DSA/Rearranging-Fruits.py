class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        data = Counter(basket1)
        for x in basket2: data[x] -= 1
        last = []
        for k,v in data.items():
            if v % 2 != 0:
                return -1
            last += [k] * abs(v // 2)
        minx = min(basket1 + basket2)
        last.sort()
        return sum(min(2*minx, x) for x in last[0:len(last)//2])
        