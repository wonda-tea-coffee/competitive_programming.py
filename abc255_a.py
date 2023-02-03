R, C = map(lambda x: int(x)-1, input().split())
A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

print(A[R][C])
