S = input()
ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        T = S[i:j]
        # print(T)
        res = True
        for k in range(len(T)):
            if not T[k] in {"A", "C", "G", "T"}:
                res = False
                break
        if res:
            ans = max(ans, len(T))

print(ans)