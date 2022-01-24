class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        dic = {}
        for i in range(numCourses):
            dic[i] = []
        for ele in prerequisites:
            dic[ele[1]].append(ele[0])
            indegree[ele[0]] += 1
        queue = []
        vis = 0
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            curr = queue.pop(0)
            vis+=1
            for i in dic[curr]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
        if vis==numCourses:
            return True
        return False
            