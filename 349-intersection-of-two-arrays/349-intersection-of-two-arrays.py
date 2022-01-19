class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dic = {}
        for i in nums1:
            if i not in dic:
                dic[i] = [1,0]
            else:
                dic[i][0] += 1
        for j in nums2:
            if j not in dic:
                dic[j] = [0,1]
            else:
                dic[j][1]+=1
        
        for key,value in dic.items():
            if value[0]>=1 and value[1]>=1:
                ans.append(key)
        return ans