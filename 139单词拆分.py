from typing import List
import copy
import math
class trie:
    def __init__(self,node_str,is_end=False):
        self.node_str=node_str
        self.is_end=is_end
        self.childs=[]
    #创建trie
    def create_trie(self,wordDict:list[str]):
        tries=[]
        for word in wordDict:
            first = next((a for a in tries if word[0]==a.node_str),None)
            if first is None:
                first=trie(word[0],len(word)==1)
            first = self.chain_change_tree(word,first,1)
            temp = [a for a in tries if not first.node_str==a.node_str]
            temp.append(first)
            tries=copy.deepcopy(temp)
        result=trie("")
        result.childs=copy.deepcopy(tries)
        return result
    def chain_change_tree(self,s,parent_node,idx):
        if len(s)==idx:
            parent_node.is_end=True
            return parent_node
        curr = next((a for a in parent_node.childs if a.node_str==s[idx]),None)
        validator = curr is None
        curr = trie(s[idx],len(s)-1==idx) if validator else curr
        new_curr = self.chain_change_tree(s,curr,idx+1)
        if validator:
            #没有则加入
            parent_node.childs.append(new_curr)
        else:
            #存在则替换
            temp_childs = [a for a in parent_node.childs if not a.node_str == curr.node_str]
            temp_childs.append(new_curr)
            parent_node.childs = copy.deepcopy(temp_childs)
        return parent_node

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp_validator(s, wordDict)

        # if len(s)==1:
        #     return s in wordDict
        # sun = trie("").create_trie(wordDict)
        # index_s = list(range(len(s)))
        # return self.validator_trie(s,sun,index_s,False,(-1,-1),False)

    #region BFS验证不通过

    # appoint[0]:开始检验的节点，
    # appoint[1]:一旦检验到这个节点则代表检验完毕
    def validator_trie(self,s,top_trie:trie,index_s,is_two,appoint,nesting):
        # s = "leetcode"，wordDict = ["lee", "t", "leetc", "code"]  leetc上一个终结的字符是e，e后面的那个t字符没有作为顶级节点被搜索过
        # s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"] and上一个终结的字符是s，s后面的那个字符a被作为顶级节点搜索过
        variable_trie=copy.deepcopy(top_trie)
        is_top=True#下一轮是否为顶层
        result=True
        record=[] #记录所有is_end为True的的节点的后一个节点的索引
        top_node_searchs=set()
        break_idx = -9 #指定节点中断一条分支的字典树的搜索
        while len(index_s)>0 and result:
            if is_top:
                variable_trie = next((a for a in top_trie.childs if a.node_str == s[index_s[0]]), None)
                if variable_trie is None:
                    #二次检验
                    result_2 = False
                    if not is_two:
                        while len(record)>0 and not result_2:
                            if record[0] not in top_node_searchs:
                                temp_range = list(range(record[0],len(s)))
                                result_2 = self.validator_trie(s,top_trie,temp_range,True,(record[0],index_s[0]),False)
                                if result_2:
                                    break_idx=record[0]
                            del record[0]
                    if result_2:
                        #更新序列
                        index_s=list(range(break_idx, len(s)))
                        variable_trie = next((a for a in top_trie.childs if a.node_str == s[index_s[0]]), None)
                    else:
                        # 验证不通过
                        result = False
                        break
                is_top = False
                top_node_searchs.add(index_s[0])
                del index_s[0]
            else:
                temp = next((a for a in variable_trie.childs if a.node_str == s[index_s[0]]), None)
                if temp is None:
                    if not variable_trie.is_end:
                        result=False
                    is_top=True
                else:
                    if variable_trie.is_end:
                        record.append(index_s[0])
                    del index_s[0]
                variable_trie=temp
            if len(index_s)>0:
                if is_two and index_s[0]==appoint[1]:
                    break
        if is_two:
            if nesting:
                return result and variable_trie.is_end
            return result
        else:
            # 二次验证字符串嵌套的类型：s = "bb"，wordDict = ["a", "b", "bbb", "bbbb"]。s="aaaaaaa"，wordDict=["aaaa","aa"]
            if variable_trie is not None:
                if not variable_trie.is_end:
                    # 二次验证
                    result_2 = False
                    while len(record) > 0 and not result_2:
                        temp_range = list(range(record[0],len(s)))
                        result_2 = self.validator_trie(s, top_trie, temp_range, True, (record[0], len(s)),True)
                        del record[0]
                    return result and result_2
            return result

    #endregion

    #region DFS验证不通过

    def many_chain_validator(self,s,parent_dic:trie):
        index=0
        temp_index=0
        while index<len(s):
            curr=next((a for a in parent_dic.childs if a.node_str==s[index]),None)
            if curr:
                if index<len(s):
                    temp_index=self.single_chain_validator(s,curr,index,[])
                    index+=temp_index+1#一定要前进
                else:
                    break
            else:
                break
        return index==len(s)

    #返回的是以bas_index为底，前进多少个索引
    #bas_index是many_chain_validator调用single_chain_validator时curr参数在s的索引
    def single_chain_validator(self, s, parent_dic: trie, bas_index,record=[]):
        if len(record)==0:
            bas_index+=1
        idx=bas_index+len(record)
        if idx<len(s):
            curr = next((a for a in parent_dic.childs if a.node_str == s[idx]), None)
            if not curr is None:
                record.append(curr.is_end)
                self.single_chain_validator(s,curr,bas_index,record)

        last_true_index = len(record) - record[::-1].index(True) if True in record else 0
        return last_true_index
    #endregion

    #region DP
    def dp_validator(self,s,wordDict):
        s_len=len(s)
        dp=[[False]*len(s) for _ in range(s_len)]
        word_dict_set=set(wordDict)
        for c in range(s_len):
            for r in range(s_len-c):
                col=c+r
                curr_str=s[r:col+1]
                validator= curr_str in word_dict_set
                if not validator:
                  for n in range(r,col):
                    validator = dp[n][r] and dp[col][n+1]
                    if validator:
                        break
                dp[col][r]=validator
        return dp[s_len-1][0]


    #endregion

s="aaaaaaa"
wordDict=["aaaa","aa"]
s = "bb"
wordDict = ["a", "b", "bbb", "bbbb"]
s="leetcode"
wordDict=["lee","t","leetc","code"]
Solution().wordBreak(s,wordDict)