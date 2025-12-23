1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        mp = {}
4        for i in strs:
5            data = "".join(sorted(i))
6            if data not in mp:
7                mp[data] = []
8            mp[data].append(i)
9        return list(mp.values())
10        