class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        flag = False
        flag1 = False
        if n<3:
            return False
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                flag1=True
            if arr[i]==arr[i-1]:
                return False
            elif arr[i]>arr[i-1] and flag==True:
                return False
            elif arr[i]<arr[i-1]:
                flag = True
                
        return True and flag and flag1