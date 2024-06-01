from typing import List, Tuple
class Solution:
    # 火被围着出不去是：1e8
    # 人被围着出不去/人被火追上-1
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        fire_map = self.getFireDistribution(grid)
        print(self.check(grid, fire_map))

    def check(self, grid: List[List[int]], fire_grid: List[List[int]]) -> int:
        fail, prptual = -1, 10 ** 9
        validator = False
        if fire_grid == None:
            if self.getFireDistribution(grid, True):
                return fail
            return prptual
        init_mid = max(fire_grid[0][1], fire_grid[1][0]) - 1
        # init_mid > 0：火不能在两分钟内到达起始点的周围，如果两分钟以内到达起始点则无法逃脱（一步死），活至少得两分钟到达人才能跑得了
        if init_mid > 0:
            r, c = len(fire_grid), len(fire_grid[0])
            left,right,mid = 0,init_mid,init_mid//2
            while left <= right:
                record_obj = {'0-0': 0}
                people_grid = [[0, 0]]
                record_grid = set()
                while len(people_grid) > 0:
                    current_x, current_y = people_grid[0][0], people_grid[0][1]
                    del people_grid[0]
                    near_nodes = []

                    # end
                    if current_x == r - 1 and current_y == c - 1:
                        validator = True
                        break
                    # top、left、bottom、right
                    for (x, y) in (current_x - 1, current_y), (current_x, current_y - 1), (current_x + 1, current_y), (current_x, current_y + 1):
                        if r > x >= 0 and c > y >= 0 == grid[x][y] and record_grid not in (x, y):
                            near_nodes.append([x, y])
                            record_grid.add((x, y))

                    for people_node in near_nodes:
                        current_time = record_obj[str(current_x) + '-' + str(current_y)] + 1
                        str_node = '-'.join(map(str, people_node))
                        if ((current_time + mid < fire_grid[people_node[0]][people_node[1]]) or
                             (current_time + mid <= fire_grid[people_node[0]][people_node[1]] and
                              people_node[0] == r - 1 and people_node[1] == c - 1)) and not ('-'.join(map(str, people_node)) in record_obj):
                            people_grid.append(people_node)
                            record_obj[str_node] = current_time
                    if validator: break
                if len(people_grid) == 0 or validator:
                    if validator:
                        left = mid + 1
                    else:
                        right = mid - 1
                    mid = (left + right) // 2
                    validator = False
            return mid
        else:
            # 火永远到不了人的周围 or 一步死
            isPeople = self.getFireDistribution(grid, True)
            if isPeople or init_mid == 0:
                # 人被围着/人和火同时被围着
                return fail
            else:
                # 火被围着
                return prptual

    def getFireDistribution(self, grid: List[List[int]], isPeople=False):
        # 绘制火源时间燃烧图/验证人是不是被围着
        mid_dict = {}
        suce_pit: List[List[int]] = []
        r, c = len(grid), len(grid[0])
        if not isPeople:
            for ritm in range(r):
                for citm in range(c):
                    if grid[ritm][citm] == 1:
                        suce_pit.append([ritm, citm])
                        mid_dict[str(ritm) + '-' + str(citm)] = 0
        else:
            suce_pit.append([0, 0])
            mid_dict['0-0'] = 0
        if len(suce_pit) > 0:
            bfs_ary, bfs_str_out = [], set()
            bfs_ary.extend(suce_pit)
            fire_map = [[-1] * c for _ in range(r)]
            while len(bfs_ary) > 0:
                current = bfs_ary[0]
                str_current = '-'.join(map(str, current))
                del bfs_ary[0]
                bfs_str_out.add(str_current)
                # top
                if current[0] > 0:
                    top = [current[0] - 1, current[1]]
                    str_top = '-'.join(map(str, top))
                    if grid[current[0] - 1][current[1]] != 2 and not (str_top in bfs_str_out) and (
                            top not in bfs_ary):
                        bfs_ary.append(top)
                        mid_dict[str_top] = mid_dict[str_current] + 1
                        fire_map[top[0]][top[1]] = mid_dict[str_top]
                # right
                if current[1] < c - 1:
                    right = [current[0], current[1] + 1]
                    str_right = '-'.join(map(str, right))
                    if grid[current[0]][current[1] + 1] not in {1, 2} and not (str_right in bfs_str_out) and (
                            right not in bfs_ary):
                        bfs_ary.append(right)
                        mid_dict[str_right] = mid_dict[str_current] + 1
                        fire_map[right[0]][right[1]] = mid_dict[str_right]
                # bottom
                if current[0] < r - 1:
                    bottom = [current[0] + 1, current[1]]
                    str_bottom = '-'.join(map(str, bottom))
                    if grid[current[0] + 1][current[1]] not in {1, 2} and not (str_bottom in bfs_str_out) and (
                            bottom not in bfs_ary):
                        bfs_ary.append(bottom)
                        mid_dict[str_bottom] = mid_dict[str_current] + 1
                        fire_map[bottom[0]][bottom[1]] = mid_dict[str_bottom]
                # left
                if current[1] > 0:
                    left = [current[0], current[1] - 1]
                    str_left = '-'.join(map(str, left))
                    if grid[current[0]][current[1] - 1] not in {1, 2} and not (str_left in bfs_str_out) and (
                            left not in bfs_ary):
                        bfs_ary.append(left)
                        mid_dict[str_left] = mid_dict[str_current] + 1
                        fire_map[left[0]][left[1]] = mid_dict[str_left]
            if isPeople:
                return fire_map[-1][-1] == -1
            else:
                return fire_map


_solution = Solution()
grid = [[0,0,1,0],[0,2,1,2],[0,0,1,0],[0,2,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
_solution.maximumMinutes(grid)
