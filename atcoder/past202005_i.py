import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
line = list(range(N))
column = list(range(N))

Q = int(input())
transpose = False
ans = []
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 3:
        transpose = not transpose
    else:
        A, B = map(lambda x: int(x)-1, q)

        if t == 1:
            if transpose:
                column[A], column[B] = column[B], column[A]
            else:
                line[A], line[B] = line[B], line[A]
        elif t == 2:
            if transpose:
                line[A], line[B] = line[B], line[A]
            else:
                column[A], column[B] = column[B], column[A]
        else:
            if transpose:
                ans.append(N*line[B]+column[A])
            else:
                ans.append(N*line[A]+column[B])

print("\n".join(map(str, ans)))
