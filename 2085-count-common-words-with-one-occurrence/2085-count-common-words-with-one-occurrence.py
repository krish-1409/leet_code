class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic = {}
        for i in words1:
            if i not in dic:
                dic[i] = [1,0]
            else:
                dic[i] = [-1,0]
        for j in words2:
            if j not in dic:
                continue
            else:
                if dic[j][0]!=-1 and dic[j][1]==0:
                    dic[j][1] = 1
                elif dic[j][1]==1:
                    dic[j][1] = -1
        ans = 0
        for key,value in dic.items():
            if value==[1,1]:
                ans+=1
        return ans