from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        sun = []
        idx = 1
        while idx < len(mountain) - 1:
            if mountain[idx] > mountain[idx - 1] and mountain[idx] > mountain[idx + 1]:
                sun.append(idx)
                idx += 2
            else:
                idx += 1
        return sun

mountain = [1,4,3,8,5]
# mountain = [1,1,3,8,5]
Solution().findPeaks(mountain)