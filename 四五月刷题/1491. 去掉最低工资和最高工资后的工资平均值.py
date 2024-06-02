from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
     sun = set(salary)
     max_val = max(sun)
     min_val = min(sun)
     sun.remove(max_val)
     sun.remove(min_val)
     result = sum(sun) / len(sun)
     return result

salary = [8000,9000,2000,3000,6000,1000]
Solution().average(salary)