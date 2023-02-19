A, B = map(int, input().split())
for x in range(1010):
    if x*8//100 == A and x//10 == B:
        print(x)
        exit()
print(-1)
