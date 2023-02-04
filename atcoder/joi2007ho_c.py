def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    S = set(P)

    ans = 0
    for i, (x1, y1) in enumerate(P):
        for x2, y2 in P[i+1:]:
            dx = x2-x1
            dy = y2-y1
            if (x1+dy, y1-dx) in S and (x2+dy, y2-dx) in S or (x1-dy, y1+dx) in S and (x2-dy, y2+dx) in S:
                ans = max(ans, dx**2 + dy**2)

    print(ans)

if __name__ == '__main__':
    main()