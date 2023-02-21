N = int(input())
cnt = [0]*(N+1)
A = list(map(int, input().split()))
for ai in A:
    cnt[ai] += 1

allsum = 0
for i in range(1, N+1):
    c = cnt[i]
    allsum += c*(c-1)//2

for ai in A:
    print(allsum - cnt[ai] + 1)
