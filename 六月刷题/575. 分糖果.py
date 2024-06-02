from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        sun = 0
        category = len(set(candyType))
        acquire = len(candyType) / 2
        if acquire >= category:
            sun = int(category)
        else :
            sun = int(acquire)
        return sun