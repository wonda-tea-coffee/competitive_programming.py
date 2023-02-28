N = int(input())
fib = [0]*(N+1)
fib[1] = fib[2] = 1
for i in range(3, N+1):
    fib[i] = (fib[i-1] + fib[i-2]) % 1000000007
print(fib[N])
