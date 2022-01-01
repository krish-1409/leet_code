class Solution:
    def fib(self, n: int) -> int:
        fib = [0] * (n+1)
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        fib[1] = 1
        fib[2] = 1
        
        for i in range(3,n+1):
            fib[i] = fib[i-1] + fib[i-2]
            
        return fib[n]