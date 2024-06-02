from typing import List
import copy

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        初始化一个数据结构的字典，是每个节点所能到达的其他节点的字典结构
        如：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]用列的字典结构为：
        {'JFK': ['SFO', 'ATL'], 'ATL': ['JFK', 'SFO'], 'SFO': ['ATL']}
        """
        Euler = {key:[] for key in list(set([n for ticket in tickets for n in ticket]))}
        for n in tickets:
            Euler[n[0]].append(n[1])
        data = self.hierholzer("JFK",Euler)
        if len(data) == 0:
            return []
        else:
            result = data[0][::-1]
        return result

    # 使用hierholzer算法
    def hierholzer(self, curr_node, Euler):
        # 当前节点后续路径集合
        curr_sides = [[]]
        if curr_node in Euler:
            # 去除重复的子节点
            child_nodes = sorted(list(set(Euler[curr_node])))
            # 如果当前节点是最终节点，但是Euler里面还有路径没走完成，说明当前这个路径不符合欧拉图
            if len(child_nodes) == 0 and len([n for item in Euler.values() for n in item]) > 0:
                return []
            record = (90,90,90)
            for node in child_nodes:
                # 对那些字典序比较靠后的进行剪枝
                node_ASCII = tuple((ord(n) for n in node))
                # 使用元组进行对比ASCII，元组对比的特性：元组之间的比较是逐个元素进行比较的，从左到右按顺序比较元组中对应位置上的元素。
                if node_ASCII > record:
                    continue
                # 在一个新的路径记录中删除当前的路径，并将其传入下级子节点
                new_euler = copy.deepcopy(Euler)
                new_euler[curr_node].remove(node)
                sides = self.hierholzer(node,new_euler)
                # 删除无用的空路径
                if [] in curr_sides:
                    curr_sides.remove([])
                # 当前节点存在有效的路径
                if len(sides) > 0:
                    if node_ASCII < record:
                        record = node_ASCII
                    # 将当前的后续路径全部加入curr_sides
                    for side in sides:
                        curr_sides.append(side)

            # 将当前节点加入自己的路径
            for side in curr_sides:
                side.append(curr_node)
        return curr_sides

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["EZE","TIA"],["EZE","HBA"],[" AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
tickets = [["JFK","ABC"],["JFK","ABC"],["ABC","DEF"],["DEF","GHI"],["GHI","JKL"],["JKL","MNO"],["MNO","PQR"],["PQR","STU"],["STU","VWX"],["VWX","YZA"],["YZA","BCD"],["BCD","EFG"],["EFG","HIJ"],["HIJ","KLM"],["KLM","NOP"],["NOP","QRS"],["QRS","TUV"],["TUV","WXY"],["WXY","MAB"],["MAB","CDE"],["CDE","FGH"],["FGH","IJK"],["IJK","LMN"],["LMN","OPQ"],["OPQ","RST"],["RST","UVW"],["UVW","XYZ"],["XYZ","ABC"],["ABC","DEF"],["DEF","GHI"],["GHI","JKL"],["JKL","MNO"],["MNO","PQR"],["PQR","STU"],["STU","VWX"],["VWX","YZA"],["YZA","BCD"],["BCD","EFG"],["EFG","HIJ"],["HIJ","KLM"],["KLM","NOP"],["NOP","QRS"],["QRS","TUV"],["TUV","WXY"],["WXY","MAB"],["MAB","CDE"],["CDE","FGH"],["FGH","IJK"],["IJK","LMN"],["LMN","OPQ"],["OPQ","RST"],["RST","UVW"],["UVW","XYZ"],["XYZ","JFK"],["XYZ","JFK"]]
Solution().findItinerary(tickets)