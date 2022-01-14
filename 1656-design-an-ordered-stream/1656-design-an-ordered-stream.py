class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.map = ["" for _ in range(self.n+1)]
        self.ptr = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        self.map[idKey] = value
        while self.ptr<=self.n and self.map[self.ptr]!="":
            ans.append(self.map[self.ptr])
            self.ptr+=1
        return ans
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)