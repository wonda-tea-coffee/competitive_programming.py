N = input()
ans = 500
pre = N[0]
hand = {"1":0,"2":0,"3":0,"4":0,"5":0, "6":1,"7":1,"8":1,"9":1,"0":1}
for i in range(1, len(N)):
    if N[i-1] == N[i]:
        ans += 301
    elif hand[N[i-1]] == hand[N[i]]:
        ans += 210
    else:
        ans += 100
print(ans)
