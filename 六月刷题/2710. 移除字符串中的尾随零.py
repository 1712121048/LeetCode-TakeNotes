class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        end_idx = 0
        for i in range(len(num)-1,0,-1):
            if num[i] != "0":
                break
            end_idx += 1
        sun = num[:len(num) - end_idx]
        return sun