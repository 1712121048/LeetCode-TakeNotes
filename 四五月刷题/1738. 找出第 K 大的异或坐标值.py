import heapq
from typing import List


class Solution:
    """
    这道题最难的是弄懂题目想表达什么？
    主要是这句：【矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。】
    看了一下英文原文的才懵懂的看出来这句话想表达什么
    这句话其实就是想表达：所有小于a行且小于b列的单元格他们异或完成之后再跟（a,b）单元格进行异或。
    你也可以理解为（a-1,b）、（a-1,b-1）、（a,b-1）这三已经异或完成之后的单元格来跟（a，b）异或，（a,b）异或完成之后将值存入（a,b）当中
    最后求整个矩形中第k大的数是多少？
    相比较而言在一个拥有一百万个单元格的无序二维数组中求出第k个大的值才费劲
    """
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        sun = []
        # 加入空白墙，避免索引超出
        matrix = [[0] + n for n in matrix]
        closure_row = [0] * len(matrix[0])
        matrix.insert(0, closure_row)
        # 行列
        row, col = len(matrix), len(matrix[0])
        # 队列快速定位（通过队列可快速定位（a,b）之前的单元格），其实手写也行毕竟才仨
        dy, dx = [0, -1, -1], [-1, -1, 0]
        for r in range(1, row):
            for c in range(1, col):
                val = matrix[r][c]
                for n in range(3):
                    val ^= matrix[r + dy[n]][c + dx[n]]
                matrix[r][c] = val
                heapq.heappush(sun, val)
                if len(sun) > k:
                    heapq.heappop(sun)
        return sun[0]

matrix = [[5,2,5],[1,8,6]]
k = 2
Solution().kthLargestValue(matrix, k)