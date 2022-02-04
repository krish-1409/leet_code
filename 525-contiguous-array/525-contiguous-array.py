class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i]==1:
                count+=1
            else:
                count-=1
            if count==0:
                ans = max(ans,i+1)
            else:
                if count not in dic:
                    dic[count] = i
                else:
                    print(i,count,dic[count])
                    ans = max(ans,i-dic[count])
        return ans