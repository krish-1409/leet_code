class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = [1,2,3,4,5,6,7,8,9]
        ans = []
        while queue and queue[0]<=high:
            
            if queue[0]>=low:
                ans.append(queue[0])
            curr = queue.pop(0)
            if curr%10!=9:
                queue.append(int(str(curr)+str(curr%10 + 1)))
        return ans