from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # 安装结束时间从小到大排序
        """
        为什么要安装右端点进行排序呢？
        因为如果按照右端点进行排序的话更容易重合（是更容易不是一定）
        而且这个也是符合直觉的，比如“某个任务必须更早的跑完，你就要优先考虑这个任务”
        既然右端点升序更容易重合那么我们就把i区间没有重合的部分在区间时间轴从后往前的执行任务
        从后往前执行任务，遇到已经重合过的点，则进行跳过
        """
        # 时间轴
        time_axis = [0] * 2002
        # 结束时间升序
        tasks.sort(key=lambda x : x[1])
        for s, e, d in tasks:
            # 找出时间轴上这个区间不大于零的点有几个
            num = sum([1 for n in time_axis[s: e + 1] if n > 0])
            # 如果时间轴的当前区间无法重合d，则对这个区间从后往前的进行执行任务
            if num < d:
                d -= num
                # 从后往前执行任务
                while d > 0:
                    # 从后往前执行任务，遇到已经重合过的点，则进行跳过
                    if time_axis[e] > 0:
                        e -= 1
                        continue
                    time_axis[e] += 1
                    d -= 1
        sun = sum([1 for n in time_axis if n > 0])
        return sun

tasks = [[3,4,1],[1,5,1],[6,6,1],[2,7,2]]
tasks = [[1,18,5],[3,15,1]]
tasks = [[14,20,5],[2,18,7],[6,14,1],[3,16,3]]
Solution().findMinimumTime(tasks)