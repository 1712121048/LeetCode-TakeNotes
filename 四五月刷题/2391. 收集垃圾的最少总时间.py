from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # 先让所以的车辆跑到最后一个房子那里。
        # 遍历过程中记录每辆车的最后到达的是哪个房子
        # 最后根据车辆最后到达的房子的索引进行多余减除
        sun = 0
        travel.insert(0,0)
        house_dic = {"M":-1,"P":-1,"G":-1}
        for i,n in enumerate(garbage):
            sun += len(n)
            sun += travel[i] * 3
            if "M" in n:
                house_dic["M"] = i
            if "P" in n:
                house_dic["P"] = i
            if "G" in n:
                house_dic["G"] = i
        # 检查M是否多余走过
        if house_dic["M"] < len(garbage) - 1:
            # 倒着数，欠下的房子个数
            debt = ((len(garbage) - 1) - house_dic["M"])
            # house_dic记录的是垃圾类别出现的最后索引，也就意味着索引之后的房子是多余出来的，现在要讲sun中对多余的减去。
            # 切片负数表示从后往前数着切
            sun -= sum(travel[-debt:])
        # 检查P是否多余走过
        if house_dic["P"] < len(garbage) - 1:
            # 倒着数，欠下的房子个数
            debt = ((len(garbage) - 1) - house_dic["P"])
            # house_dic记录的是垃圾类别出现的最后索引，也就意味着索引之后的房子是多余出来的，现在要讲sun中对多余的减去。
            # 切片负数表示从后往前数着切
            sun -= sum(travel[-debt:])
        # 检查G是否多余走过
        if house_dic["G"] < len(garbage) - 1:
            # 倒着数，欠下的房子个数
            debt = ((len(garbage) - 1) - house_dic["G"])
            # house_dic记录的是垃圾类别出现的最后索引，也就意味着索引之后的房子是多余出来的，现在要讲sun中对多余的减去。
            # 切片负数表示从后往前数着切
            sun -= sum(travel[-debt:])
        return sun