class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last = second_last = -1
        lastCount = curr = res = 0
        for i in fruits:
            if i == last or i == second_last:
                curr += 1
            else:
                curr = lastCount + 1
            
            if i == last:
                lastCount += 1
            else:
                lastCount = 1
                second_last, last = last, i
            res = max(res, curr)
        return res

        