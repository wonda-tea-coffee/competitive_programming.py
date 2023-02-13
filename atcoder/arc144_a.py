N = int(input())
print(2*N)

if N % 4 > 0:
    print(str(N % 4) + "4" * (N//4))
else:
    print("4" * (N//4))