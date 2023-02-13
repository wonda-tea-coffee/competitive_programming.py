import heapq

N = int(input())
A = list(map(int, input().split()))

k = 0
odd = []
for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2
        k += 1

    heapq.heappush(odd, A[i])

for i in range(k):
    temp = heapq.heappop(odd)
    heapq.heappush(odd, 3*temp)
print(heapq.heappop(odd))
