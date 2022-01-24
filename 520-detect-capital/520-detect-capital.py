class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        caps = 0
        for i in range(n):
            if ord('A')<=ord(word[i])<=ord('Z'):
                caps+=1
        if ord('A')<=ord(word[0])<=ord('Z'):
            if n==caps or caps==1:
                return True
        elif caps==0:
            return True
        return False