class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answerKey = answerKey.replace(' ','')
        # 双指针
        left, right = 0, 0
        # T 和 F 在双指针区间出现的情况
        dic_info = { "T": 0, "F": 0 }

        sun = 0
        while right < len(answerKey):
            curr = answerKey[right]
            # 入库
            dic_info[curr] += 1
            # 更新右指针
            right += 1
            # T and F 都不符合 k 要求
            if dic_info["T"] > k and dic_info["F"] > k:
                # 左移左指针
                for i in range(left, right):
                    # 对 T and F 进行出库
                    if answerKey[i] == 'T':
                        dic_info["T"] -= 1
                    else:
                        dic_info["F"] -= 1

                    if dic_info["T"] <= k or dic_info["F"] <= k:
                        # T and F 中只要有一个符合要求就停止左滑动
                        left = i + 1
                        break
            # 此处 T 和 F 都符合 k 的要求
            sun = max(right - left, sun)
        return sun

answerKey = "FTTTFTTTF T FFFFFTFFFT"
answerKey = "TTTFTTTFT FFFFFTFFFT"
answerKey = "TTTF TTTF TFTFF"
answerKey = "TTFF"
k = 2
Solution().maxConsecutiveAnswers(answerKey, k)