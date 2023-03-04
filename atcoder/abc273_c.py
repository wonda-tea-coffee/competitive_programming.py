from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = sorted(Counter(A).items(), reverse=True)

for _, ci in c:
    print(ci)
for i in range(N-len(c)):
    print(0)
