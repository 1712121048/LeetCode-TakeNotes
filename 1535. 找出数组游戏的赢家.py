from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 根据题意可得擂主的位置永远在arr[0]
        challenge_main_val, challenge_main_k = arr[0], 0
        while challenge_main_k < k and challenge_main_k < len(arr):
            # 第一个字段的值，第二个字段的值
            # [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
            # [3,2,1]
            challenge = arr[1]
            if challenge > challenge_main_val:
                # 出现新的擂主
                # 更新霸擂次数，更新擂主
                challenge_main_k = 1
                challenge_main_val = challenge
                # 淘汰老擂主
                arr.append(arr.pop(0))
            else:
                # 霸擂
                challenge_main_k += 1
                # 更新失败的的位置，为下一个挑战者让路
                arr.append(arr.pop(1))
        return challenge_main_val

arr = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99]
k = 99
arr = [2,1,3,5,4,6,7]
k = 2
Solution().getWinner(arr, k)


