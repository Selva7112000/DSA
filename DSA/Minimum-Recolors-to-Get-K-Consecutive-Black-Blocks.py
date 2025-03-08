class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        print(blocks[:k])
        w = blocks[:k].count("W")
        s = w 
        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                w += 1
            if blocks[i - k] == "W" :
                w -=1 
            s = min(s,w)
        return s
        