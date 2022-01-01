class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        ans = []
        n = len(nums)
        for i in range(k):
            while queue and queue[-1][1]<=nums[i]:
                queue.pop()
            queue.append([i,nums[i]])
        ans.append(queue[0][1])
        for i in range(k,n):
            while queue and queue[0][0]<=i-k:
                queue.pop(0)
            while queue and queue[-1][1]<=nums[i]:
                queue.pop()
            queue.append([i,nums[i]])
            ans.append(queue[0][1])
        return ans
                