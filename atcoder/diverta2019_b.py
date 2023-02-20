R, G, B, N = map(int, input().split())

ans = 0
for r in range(0,N+1,R):
    for g in range(0,N+1,G):
        if r+g > N: break
        if (N-r-g)%B==0:
            # print(r//R, g//G, (N-r-g)//B)
            ans += 1
print(ans)
