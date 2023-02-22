N, K = map(int, input().split())
p = list(map(lambda x: (int(x)+1)/2, input().split()))
psum = [0]
for pi in p:
    psum.append(psum[-1] + pi)

ans = 0
for i in range(N-K+1):
    ans = max(ans, psum[i+K] - psum[i])

print(ans)
