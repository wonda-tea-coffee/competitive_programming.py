N, M = map(int, input().split())
A = [list(input()) for _ in range(2*N)]

win = [0]*(2*N)
t = str.maketrans("GCP", "012")

def ranking(win):
    score = []
    for i in range(2*N):
        score.append((-win[i], i))
    score.sort()

    h = {}
    for rank, (_, i) in enumerate(score):
        h[rank] = i

    return h

for i in range(M):
    # print("Round:", i+1)
    r = ranking(win)
    for k in range(N):
        a = r[2*k]
        b = r[2*k+1]
        ta = int(A[a][i].translate(t))
        tb = int(A[b][i].translate(t))
        # print(" ", a+1, b+1)
        if (ta+1)%3 == tb:
            # print("    win:", a+1)
            win[a] += 1
        elif (tb+1)%3 == ta:
            # print("    win:", b+1)
            win[b] += 1

r = ranking(win)
# print(r)
for i in range(2*N):
    print(r[i]+1)
