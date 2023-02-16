import heapq

N = int(input())
A = list(map(int, input().split()))
k = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] //= 2
        k += 1

heapq.heapify(A)
for i in range(k):
    t = heapq.heappop(A)
    heapq.heappush(A, t*3)

print(heapq.heappop(A))
