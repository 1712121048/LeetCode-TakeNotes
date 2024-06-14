import bisect
from typing import List

# limit >= max(people)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sun = 0
        if len(people) < 2:
            sun = 1
        else:
            people.sort()
            # 双指针（left永远等于 0）
            left = 0
            right = max(bisect.bisect_right(people, limit - people[left]) - 1, 0)
            while True:
                if left == right:
                    people.pop(left)
                else:
                    people.pop(right)
                    people.pop(left)
                sun += 1
                if len(people) == 0:
                    break
                right = max(bisect.bisect_right(people, limit - people[left]) - 1, 0)
        return sun

class Solution2:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sun = 0
        if len(people) < 2:
            sun = 1
        else:
            people.sort()
            # p = people，l = left， r = right
            # p[l] 所能加的最大值。 p[r] 是否为在（p[l] + p[r]）小于等于 limit 的前提下，p[l] 所能加的最大值最大的情况
            validator = False
            # 双指针
            left, right = 0, 1
            # 核心目的就是让 right == max(bisect.bisect_right(people, limit - people[left]) - 1, 0)
            while len(people) > 0:
                if len(people) == 1:
                    sun += 1
                    break
                if people[left] + people[right] <= limit or validator:
                    if not validator:
                        if right == len(people) - 1 or people[left] + people[right] == limit:
                            # 已经到达了，people[left] 能加的最大的值了，但是双指针相加还是小于 limit，那么就选择当前 right
                            validator = True
                        else:
                            right += 1

                    if validator:
                        people.pop(left)
                        if right > left:
                            people.pop(right - 1)
                        sun += 1
                        right = 1
                        validator = False

                elif people[left] + people[right] > limit:
                    right -= 1
                    validator = True
        return sun

people = [50,50,50,68,92]
limit = 100

# people = [1,1,1,2,2,4]
# limit = 4

# people = [1,1,1,1,2,2,4]
# limit = 7

# people = [1,1,1,2,2,6]
# limit = 6

# people = [1,1,6,6]
# limit = 9
#
# people = [3,21,20,1]
# limit = 22

Solution().numRescueBoats(people, limit)