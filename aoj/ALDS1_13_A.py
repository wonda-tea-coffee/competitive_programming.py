import itertools
import copy

def check(S):
    for i in range(8):
        for j in range(8):
            if not S[i][j]: continue

            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                ni = i
                nj = j
                while 0 <= ni + dy < 8 and 0 <= nj + dx < 8:
                    ni += dy
                    nj += dx
                    # print(ni, nj, S[ni][nj])
                    if S[ni][nj]:
                        return False

    return True

def show(S):
    for i in range(8):
        for j in range(8):
            if S[i][j]:
                print("Q", end="")
            else:
                print(".", end="")
        print()

k = int(input())
G = [[False]*8 for _ in range(8)]
q = []
for _ in range(k):
    r, c = map(int, input().split())
    G[r][c] = True
    q.append((r, c))

for i in itertools.permutations(range(8)):
    S = copy.deepcopy(G)
    ki = 0
    for j in range(8):
        if S[j][i[j]]: ki += 1
        S[j][i[j]] = True
    if ki == k and check(S):
        show(S)
        break
