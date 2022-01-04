class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = bin(n)[2:][::-1]
        ans = 0
        count = 0
        for x in s:
            ans+=(2**count)*(1-int(x))
            count+=1
        return ans