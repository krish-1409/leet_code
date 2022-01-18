def getComb(words,temp):

    if len(words)==0:
        if temp=="":
            return
        getComb.ans.append(temp)
        return
    for i in words[0]:
        getComb(words[1:],temp+i)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        words = []
        for i in digits:
            words.append(dic[i])
        getComb.ans = []
        getComb(words,'')
        return getComb.ans