class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i,j = 0,n-1
        while i<=j:
            
            if nums[i]==val:
                nums[i],nums[j] = nums[j], nums[i]
                j-=1
                i-=1
            i+=1
        
        return j+1
            